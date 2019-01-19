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
    
    def test_can_handle_fractions(self):
        res = self.calculator.calculate("1 / 2")
        self.assertAlmostEqual(res, 0.5)

    def test_operations_have_correct_priority(self):
        res = self.calculator.calculate("1 + 2 * 2 + 2 ^ 2 * 2")
        self.assertEqual(res, 13)

    def test_can_calculate_unpadded_expressions(self):
        exp = "(6/2)*(2+1)"
        res = self.calculator.calculate(exp)
        self.assertEqual(res, 9)

    def test_can_handle_strange_braces(self):
        exp1 = "(2)+(2)"
        exp2 = "(((((((((( 1 + 1 ))))))))))"
        res1 = self.calculator.calculate(exp1)
        res2 = self.calculator.calculate(exp2)
        self.assertEqual(res1, 4)
        self.assertEqual(res2, 2)

    def test_can_parse_functions(self):
        exp1 = "sin(0)"
        res1 = self.calculator.to_rpn(exp1)
        self.assertEqual(res1, ["0","sin"])

    def can_calculate_functions(self):
        exp1 = "sin(0)"
        exp2 = "3 * cos(0)"
        res1 = self.calculator.calculate(exp1)
        res2 = self.calculator.calculate(exp2)
        self.assertAlmostEqual(exp1, 0)
        self.assertAlmostEqual(exp2, 3)

    def test_functions_can_have_expression_arguments(self):
        expressioin = "sin(3 * 0)"
        res = self.calculator.calculate(expressioin)
        expression2 = "sin( sin( 0 ) )"
        res2 = self.calculator.calculate(expression2)
        
        self.assertEqual(res, 0)
        self.assertEqual(res2, 0)

    if __name__ == '__main__':
        unittest.main()

