class Heatmap:
    def __init__(self):
        self.zone_density = {}  # zone_id -> count

    def update(self, zone_id, people_count):
        self.zone_density[zone_id] = people_count
        return self.zone_density

    def level(self, count):
        if count >= 5:
            return "RED"
        elif count >= 3:
            return "YELLOW"
        else:
            return "GREEN"

    def color(self, count):
        if count >= 5:
            return "RED"
        elif count >= 3:
            return "YELLOW"
        else:
            return "GREEN"
