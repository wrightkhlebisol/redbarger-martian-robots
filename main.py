import sys
from src.parser import parse_input

def main():
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], 'r') as f:
            input_data = f.read()
    else:
        print("Enter input (press Ctrl+D when done):")
        input_data = sys.stdin.read()

    robots = parse_input(input_data)

    for robot in robots:
        print(robot)


if __name__ == "__main__":
    main()
