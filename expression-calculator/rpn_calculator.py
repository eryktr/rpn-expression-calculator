from input_parser import InputParser
from validator import Validator
from rpn_processor import RPNProcessor

class RPNCalculator:
    
    def __init__(self):
        self.parser = InputParser()
        self.processor = RPNProcessor()

    def to_rpn(self, expression):
        try:
            return self.parser.to_rpn(expression)
        except ValueError:
            raise
        
    def calculate(self, expression, value = 0):
        try:
            rpn = self.to_rpn(expression)
            return self.processor.evaluate_rpn(rpn, value)
        except ValueError:
            print("Your expression is invalid")
        except ZeroDivisionError:
            print("Can't divide by zero.")
    
    def evaluate(self, expression, value):
        return self.calculate(expression, value)
