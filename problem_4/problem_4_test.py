import unittest
from problem_4 import countNumberOfOnes

class TestStringMethods(unittest.TestCase):

    def testCountNumberOfOnes(self):
        self.assertEqual(countNumberOfOnes(0), -1, 'countNumberOfOnes(0) should return -1')
        self.assertEqual(countNumberOfOnes(1), 1, 'countNumberOfOnes(1) should return 1')
        self.assertEqual(countNumberOfOnes(8), 1, 'countNumberOfOnes(8) should return 1')
        self.assertNotEqual(countNumberOfOnes(8), 2, 'countNumberOfOnes(8) should not return 2')
        self.assertEqual(countNumberOfOnes(10), 2, 'countNumberOfOnes(10) should return 2')
        self.assertEqual(countNumberOfOnes(11), 4, 'countNumberOfOnes(11) should return 4')
        self.assertNotEqual(countNumberOfOnes(11), 6, 'countNumberOfOnes(11) should not return 6')
        self.assertEqual(countNumberOfOnes(17), 10, 'countNumberOfOnes(17) should return 10')
        self.assertEqual(countNumberOfOnes(21), 13, 'countNumberOfOnes(21) should return 13')

if __name__ == '__main__':
    unittest.main()