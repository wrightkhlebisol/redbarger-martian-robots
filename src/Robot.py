class Robot:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.lost = False

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.orientation)
        self.orientation = directions[(current_index + 1) % 4] # modulo division to wrap around directions

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.orientation)
        self.orientation = directions[(current_index + 1) % 4]

    def get_next_position(self):
        next_x, next_y = self.x, self.y

        if self.orientation == 'N':
            next_y += 1
        elif self.orientation == 'S':
            next_y -= 1
        elif self.orientation == 'E':
            next_x += 1
        else:
            next_x -= 1

        return next_x, next_y

    def __str__(self):
        result = f"{self.x} {self.y} {self.orientation}"
        if self.lost:
            result += " LOST"
        return result
