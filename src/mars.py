class Mars:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.scents = set()

    def is_within_bounds(self, x, y):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def has_scent(self, x, y):
        return (x, y) in self.scents

    def add_scent(self, x, y):
        self.scents.add((x, y))

    def process_robot(self, robot, instructions):
        for instruction in instructions:
            if robot.lost:
                break

            if instruction == 'L':
                robot.turn_left()
            elif instruction == 'R':
                robot.turn_right()
            elif instruction == 'F':
                next_x, next_y = robot.get_next_position()

                if self.is_within_bounds(next_x, next_y):
                    robot.x = next_x
                    robot.y = next_y
                else:
                    if not self.has_scent(robot.x, robot.y):
                        robot.lost = True
                        self.add_scent(robot.x, robot.y)

        
        return robot                
