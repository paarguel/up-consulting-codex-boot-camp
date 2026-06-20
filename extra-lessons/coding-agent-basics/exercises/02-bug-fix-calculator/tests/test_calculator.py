import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "starter"))

from calculator import add, subtract, divide, percent_of


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self):
        self.assertEqual(divide(12, 3), 4)

    def test_divide_by_zero_has_clear_error(self):
        with self.assertRaises(ValueError):
            divide(12, 0)

    def test_percent_of(self):
        self.assertEqual(percent_of(200, 10), 20)


if __name__ == "__main__":
    unittest.main()
