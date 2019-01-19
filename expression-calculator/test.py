import unittest
from rpn_calculator import RPNCalculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = RPNCalculator()

    def test_simple_operations(self):
        sum = self.calculator.calculate("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10")
        diff = self.calculator.calculate("20 - 1 - 1 - 3 - 10")
        prod = self.calculator.calculate("1 * 1 * 1 * 1 * 5 * 1 * 2")
        quot = self.calculator.calculate("100 / 10 / 2")
        pow = self.calculator.calculate("2 ^ 10")
        
        self.assertEqual(sum, 55)
        self.assertEqual(diff, 5)
        self.assertEqual(prod, 10)
        self.assertEqual(quot, 5)
        self.assertEqual(pow, 1024)
    
    def test_can_calculate_unpadded_expressions(self):
        exp = "(6/2)*(2+1)"
        res = self.calculator.calculate(exp)
        self.assertEqual(res, 9)

    if __name__ == '__main__':
        unittest.main()

