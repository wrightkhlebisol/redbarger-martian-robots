class Mars:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.scents = set()

    def is_within_bounds(self, x, y):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y


