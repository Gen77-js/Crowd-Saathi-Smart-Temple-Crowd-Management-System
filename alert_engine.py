import time

class AlertEngine:
    def __init__(self):
        self.zone_limits = {
            "Z1": 4,
            "Z2": 2,
            "Z3": 30
        }

        self.last_counts = {}
        self.last_time = time.time()
        self.alerts = []

    def check(self, zone_data):
        current_time = time.time()
        alerts_now = []

        for zone, count in zone_data.items():
            limit = self.zone_limits.get(zone, 999)

            # ALERT 1: LIMIT CROSS
            if count >= limit:
                alerts_now.append({
                    "zone": zone,
                    "type": "OVER_CROWD",
                    "message": f"Zone {zone} overcrowded ({count})"
                })

            # ALERT 2: SUDDEN INCREASE
            last = self.last_counts.get(zone, count)
            if count - last >= 5:
                alerts_now.append({
                    "zone": zone,
                    "type": "SUDDEN_SURGE",
                    "message": f"Sudden crowd surge in {zone}"
                })

            self.last_counts[zone] = count

        self.last_time = current_time
        self.alerts = alerts_now
        return alerts_now
