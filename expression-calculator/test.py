from input_parser import InputParser
from rpn_processor import RPNProcessor

parser = InputParser()
processor = RPNProcessor()

def calculate(expression):
    rpn = parser.to_rpn(expression)
    print("in RPN: ", rpn)
    return processor.evaluate_rpn(rpn)


while (True):
    expression = input("")
    print("You entered: ", expression)
    res = calculate(expression)
    print(res)

