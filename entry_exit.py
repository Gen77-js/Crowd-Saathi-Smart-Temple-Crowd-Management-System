class EntryExitCounter:
    def __init__(self, line_y):
        self.line_y = line_y
        self.total_in = 0
        self.total_out = 0

        self.track_memory = {}     # objectID -> last_y
        self.counted_in = set()    # IDs already entered
        self.counted_out = set()   # IDs already exited

    def update(self, objects):
        """
        objects = { objectID : (cX, cY) }
        """

        for objectID, centroid in objects.items():
            current_y = centroid[1]

            if objectID not in self.track_memory:
                self.track_memory[objectID] = current_y
                continue

            previous_y = self.track_memory[objectID]

            # ENTRY condition (top -> bottom)
            if previous_y < self.line_y and current_y >= self.line_y:
                if objectID not in self.counted_in:
                    self.total_in += 1
                    self.counted_in.add(objectID)

            # EXIT condition (bottom -> top)
            elif previous_y > self.line_y and current_y <= self.line_y:
                if objectID not in self.counted_out:
                    self.total_out += 1
                    self.counted_out.add(objectID)

            self.track_memory[objectID] = current_y

        return self.total_in, self.total_out
