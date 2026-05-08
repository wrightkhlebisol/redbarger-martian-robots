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

    
