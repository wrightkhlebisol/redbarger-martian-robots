from src.input_parser import parse_input


def main():
    sample_input = """5 3
    1 1 E
    RFRFRFRF

    3 2 N
    FRRFLLFFRRFLL

    0 3 W
    LLFFFLFLFL"""

    robots = parse_input(sample_input)
    
    for robot in robots:
        print(robot)


if __name__ == "__main__":
    main()
