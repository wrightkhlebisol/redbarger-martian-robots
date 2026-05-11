# Martian Robots Solution

A Python implementation of the Martian Robots coding challenge.

## Running the Solution

### Run with sample input file:
```bash
python3 -m main sample_input.txt
```

### Run with custom input:
```bash
python3 -m main < your_input.txt
```

### Run interactively:
```bash
python3 -m main
# Then enter your input in the format

5 3
1 1 E
RFRFRFRF

3 2 N
FRRFLLFFRRFLL

0 3 W
LLFFFLFLFL

# and press Ctrl+D when done
```

## Running Tests

```bash
python3 -m test_martian_robots.py -v
```

## Implementation Details

The solution follows YAGNI principles with a clean, minimal implementation:

- `Robot` class: Handles robot state (position, orientation) and turning logic
- `Mars` class: Manages the grid, bounds checking, and scent tracking
- `parse_input()`: Processes the input format
- Comprehensive unit tests covering all edge cases

The scent mechanism prevents robots from falling off at locations where previous robots were lost.
