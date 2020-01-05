import unittest
from Cal import Calculator
class testCal(unittest.TestCase):
    def test_add(self):
        ca=Calculator(2,3)
        self.assertEqual(ca.add(),5, msg='Add 2 numbers')

if __name__ == '__main__':
    unittest.main()