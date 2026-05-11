import unittest
from src.robot import Robot
from src.mars import Mars

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

    def test_robot_string_representation(self):
        robot = Robot(1, 2, 'N')
        self.assertEqual(str(robot), "1 2 N")

        robot.lost = True
        self.assertEqual(str(robot), "1 2 N LOST")


class TestMars(unittest.TestCase):
    def test_is_within_bounds(self):
        mars = Mars(5, 3)

        self.assertTrue(mars.is_within_bounds(0, 0))
        self.assertTrue(mars.is_within_bounds(5, 3))
        self.assertTrue(mars.is_within_bounds(2, 2))

        self.assertFalse(mars.is_within_bounds(-1, 0))
        self.assertFalse(mars.is_within_bounds(6, 0))
        self.assertFalse(mars.is_within_bounds(0, -1))
        self.assertFalse(mars.is_within_bounds(0, 4))

    def test_has_scent(self):
        mars = Mars(5, 3)

        self.assertFalse(mars.has_scent(3, 3))

        mars.add_scent(3, 3)
        self.assertTrue(mars.has_scent(3, 3))

        mars.add_scent(3, 3)
        self.assertTrue(mars.has_scent(3, 3))

    def test_process_basic_movement(self):
        mars = Mars(5, 3)
        robot = Robot(1, 1, 'E')

        mars.process_robot(robot, 'F')
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.orientation, 'E')

        mars.process_robot(robot, 'L')
        self.assertEqual(robot.orientation, 'N')

        mars.process_robot(robot, 'F')
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 2)

    def test_process_robot_falling_off(self):
        mars = Mars(5, 3)
        robot = Robot(3, 2, 'N')

        mars.process_robot(robot, 'FRRFLLFFRRFLL')

        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.orientation, 'N')
        self.assertTrue(robot.lost)
        self.assertTrue(mars.has_scent(3, 3))



if __name__ == '__main__':
    unittest.main()


