import unittest
from main import sum_digits


class MyTestCase(unittest.TestCase):
    def test_values(self):
        self.assertEqual(sum_digits(11), 2)
        self.assertEqual(sum_digits(24), 6)
        self.assertEqual(sum_digits(99), 18)

    def test_wrong_type(self):
        with self.assertRaises(AttributeError):
            sum_digits("string")
        with self.assertRaises(AttributeError):
            sum_digits(False)
        with self.assertRaises(AttributeError):
            sum_digits(1.001)


if __name__ == '__main__':
    unittest.main()
