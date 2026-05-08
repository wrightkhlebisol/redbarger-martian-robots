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


    def test_turn_right(self):
        robot = Robot(0, 0, 'N')
        robot.turn_right()
        self.assertEqual(robot.orientation, 'E')

        robot.turn_right()
        self.assertEqual(robot.orientation, 'S')

        robot.turn_right()
        self.assertEqual(robot.orientation, 'W')

        robot.turn_right()
        self.assertEqual(robot.orientation, 'N')


    def test_get_next_position(self):
        robot = Robot(2, 2, 'N')
        self.assertEqual(robot.get_next_position(), (2, 3))

        robot.orientation = 'E'
        self.assertEqual(robot.get_next_position(), (3, 2))

        robot.orientation = 'W'
        self.assertEqual(robot.get_next_position(), (1, 2))

        robot.orientation = 'S'
        self.assertEqual(robot.get_next_position(), (2, 1))


if __name__ == '__main__':
    unittest.main()


