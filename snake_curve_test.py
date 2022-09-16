import unittest

from snake_curve import SnakeCurve
from dimension import Dimension
from coordinate import Coordinate

class TestSnakeCurve(unittest.TestCase):
    def test_get_d(self):
        snake_curve = SnakeCurve(25, Dimension(5, 5))
        self.assertEqual(snake_curve.get_number_of_elements(), 25)
        self.assertEqual(snake_curve.get_d(Coordinate(2, 3)), 17)
        self.assertEqual(snake_curve.get_d(Coordinate(6, 6)), -1)
        self.assertEqual(snake_curve.get_d(Coordinate(5, 5)), -1)
        self.assertEqual(snake_curve.get_d(Coordinate(4, 4)), 24)

    def test_get_coordinate(self):
        snake_curve = SnakeCurve(25, Dimension(5, 5))
        self.assertEqual(snake_curve.get_coordinate(17).get_x(), 2)
        self.assertEqual(snake_curve.get_coordinate(17).get_y(), 3)
        self.assertEqual(snake_curve.get_coordinate(24).get_x(), 4)
        self.assertEqual(snake_curve.get_coordinate(24).get_y(), 4)



if __name__ == '__main__':
    unittest.main()
