import unittest
from Problem_5 import Reverse_Pairs

class TestStringMethods(unittest.TestCase):

    def test_Reverse_Pairs(self):
        self.assertEqual(Reverse_Pairs([0, 0, 0]), 0, 'Reverse_Pairs should return 0')
        self.assertEqual(Reverse_Pairs([1, 0, 0]), 2, 'Reverse_Pairs should return 2')
        self.assertEqual(Reverse_Pairs([0, 1, 2, 3, 4, 5]), 0, 'Reverse_Pairs should return 0')
        self.assertEqual(Reverse_Pairs([5, 4, 3, 2, 1]), 4, 'Reverse_Pairs should return 4')
        self.assertEqual(Reverse_Pairs([10, 1, 1, 1, 1, 1]), 5, 'Reverse_Pairs should return 5')
        self.assertEqual(Reverse_Pairs([1]), 0, 'Reverse_Pairs should return 0')
        self.assertEqual(Reverse_Pairs([0, 10, 1, 4, 5, 0]), 6, 'Reverse_Pairs should return 6')
        self.assertEqual(Reverse_Pairs([-1, 0, 0, 0]), 0, 'Reverse_Pairs should return 0')
        self.assertEqual(Reverse_Pairs([0, 0, -25]), 2, 'Reverse_Pairs should return 0')

if __name__ == '__main__':
    print("Starting Testing")
    unittest.main()