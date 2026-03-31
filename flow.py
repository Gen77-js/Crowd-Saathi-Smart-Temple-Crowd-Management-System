class DirectionFlow:
    def __init__(self):
        self.last_zone = {}   # objectID -> zone
        self.flow_count = {}  # "North->Center" : count

    def update(self, objects, current_zone):
        """
        objects: {objectID: (cX, cY)}
        current_zone: zone_id for this camera
        """
        for objectID in objects.keys():
            prev_zone = self.last_zone.get(objectID)

            if prev_zone and prev_zone != current_zone:
                key = f"{prev_zone}->{current_zone}"
                self.flow_count[key] = self.flow_count.get(key, 0) + 1

            self.last_zone[objectID] = current_zone

        return self.flow_count
