import unittest
from src.robot import Robot

class TestRobot(unittest.TestCase):
    def test_turn_left(self):
        robot = Robot(0, 0, 'N')
        robot.turn_left()
        self.assertEqual(robot.orientation, 'W')

        robot.turn_left()
        self.assertEqual(robot.orientation, 'S')

        robot.turn_left()
        self.assertEqual(robot.orientation, 'E')

        robot.turn_left()
        self.assertEqual(robot.orientation, 'N')


if __name__ == '__main__':
    unittest.main()


