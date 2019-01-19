from input_parser import InputParser
from validator import Validator
from rpn_processor import RPNProcessor

class RPNCalculator:
    
    def __init__(self):
        self.parser = InputParser()
        self.processor = RPNProcessor()

    def to_rpn(self, expression):
        return self.parser.to_rpn(expression)
        
    def calculate(self, expressioin):
        rpn = self.parser.to_rpn(expressioin)
        return self.processor.evaluate_rpn(rpn)
