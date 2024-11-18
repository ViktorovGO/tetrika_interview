import unittest
from solution import sum_two
class TestDec(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum_two(15,5), 20)
        self.assertNotEqual(sum_two(15,3), 20)
        self.assertNotEqual(sum_two(45,-32), 1)

    def test_error(self):
        self.assertRaises(TypeError, sum_two, 5, "10")
        self.assertRaises(TypeError, sum_two, "2", "10")
        self.assertRaises(TypeError, sum_two, True, "10")
        self.assertRaises(TypeError, sum_two, [123], "10")
        self.assertRaises(TypeError, sum_two, (12,32,67), "5")
        self.assertRaises(TypeError, sum_two, {'k':5}, 4)
        self.assertRaises(TypeError, sum_two, 5.2, 13)

if __name__ == '__main__':
    unittest.main()