import unittest
from src.parser import parse_input

class TestIntegration(unittest.TestCase):
    def test_sample_input(self):
        sample_input = """5 3
        1 1 E
        RFRFRFRF

        3 2 N
        FRRFLLFFRRFLL

        0 3 W
        LLFFFLFLFL"""

        robots = parse_input(sample_input)

        self.assertEqual(len(robots), 3)
        self.assertEqual(str(robots[0]), "1 1 E")
        self.assertEqual(str(robots[1]), "3 3 N LOST")
        self.assertEqual(str(robots[2]), "2 3 S")

if __name__ == "__main__":
    unittest.main()
