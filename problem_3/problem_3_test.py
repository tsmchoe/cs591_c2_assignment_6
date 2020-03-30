import unittest
from problem_3 import string_multiplication

class TestStringMethods(unittest.TestCase):

    def test_string_multiplication(self):
        self.assertEqual(string_multiplication('0','0'), '0', 'string_multiplication("0","0") should return "0"')
        self.assertEqual(string_multiplication('12','6'), '18', 'string_multiplication("12","6") should return "18"')
        self.assertNotEqual(string_multiplication('0','0'), 0, 'string_multiplication("0","0") should not return 0')
        self.assertNotEqual(string_multiplication('12','6'), 18, 'string_multiplication("12","6") should not return 18')
        self.assertEqual(string_multiplication('7598','1339130'), '1346728', 'string_multiplication("7598","1339130") should return "1346728"')
        self.assertEqual(string_multiplication('503','30'), '533', 'string_multiplication("503","30") should return "533"')

if __name__ == '__main__':
    unittest.main()