from src.robot import Robot
from src.mars import Mars

def parse_input(input_text):
    lines = input_text.strip().split('\n')

    grid_size = lines[0].split()
    max_x, max_y = int(grid_size[0]), int(grid_size[1])
    mars = Mars(max_x, max_y)

    robots = [] # Hold processed robots
    i = 1 # line 1 is the first robot position
    while i < len(lines):
        if lines[i].strip(): # non-empty line
            position_parts = lines[i].split()
            x = int(position_parts[0])
            y = int(position_parts[1])
            orientation = position_parts[2]

            robot = Robot(x, y, orientation)

            if i + 1 < len(lines): # Check next line in range
                instructions = lines[i + 1].strip()
                mars.process_robot(robot, instructions)
                robots.append(robot)

            i += 2
        else: # empty line
            i += 1

    return robots
