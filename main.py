import cv2
import json
from detector import detect_and_track, tracker
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import threading
import logging
from alert_engine import AlertEngine
from entry_exit import EntryExitCounter
from flow import DirectionFlow
from heatmap import Heatmap

logging.basicConfig(level=logging.DEBUG)


# INIT
app = Flask(__name__, static_folder="static")
CORS(app)

flow_engine = DirectionFlow()
heatmap_engine = Heatmap()
alert_engine = AlertEngine()

system_data = {
    "zones": {},
    "flows": {},
    "total": 0
}
system_data["alerts"] = []


# CAMERA THREAD FUNCTION
def camera_thread(cam_info):
    cap = cv2.VideoCapture(cam_info["source"])
    zone = cam_info["zone_id"]

    entry_exit = EntryExitCounter(line_y=250)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, objects = detect_and_track(frame)

        in_c, out_c = entry_exit.update(objects)
        count = len(objects)

        flows = flow_engine.update(objects, zone)
        zones = heatmap_engine.update(zone, count)

        system_data["zones"] = zones
        system_data["flows"] = flows
        system_data["total"] = sum(zones.values())
        alerts = alert_engine.check(zones)
        system_data["alerts"] = alerts

        cv2.line(frame, (250, 0), (250, frame.shape[0]), (0, 0, 255), 2)
        cv2.putText(frame, f"IN:{in_c} OUT:{out_c}",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 0, 255), 2)

        cv2.imshow(zone, frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()


# LOAD CAMERAS & START THREADS
with open("cameras/cam_config.json") as f:
    cams = json.load(f)

for cam in cams.values():
    threading.Thread(target=camera_thread, args=(cam,), daemon=True).start()


# API FOR ADMIN / APP
@app.route("/")
def admin_panel():
    return send_from_directory("static", "admin.html")


@app.route("/api/status")
def status():
    logging.debug(f"API called - system_data: {system_data}")
    response_zones = {}
    for zone, count in system_data["zones"].items():
        response_zones[zone] = {
            "count": count,
            "level": heatmap_engine.level(count)
        }

    return jsonify({
        "total": system_data["total"],
        "zones": response_zones,
        "flows": system_data["flows"],
        "alerts": system_data.get("alerts", [])
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
