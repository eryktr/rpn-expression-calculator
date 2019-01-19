from stack import Stack
from validator import Validator
class RPNProcessor:
    operator_operation_map = {
        '+' : lambda a, b : b + a,
        '-' : lambda a, b : b - a,
        '*' : lambda a, b : b * a,
        '/' : lambda a, b : b / a,
        '^' : lambda a, b : b ** a
    }
    
    def evaluate_rpn(self, input):
        number_stack = Stack()
        for token in input:
            if Validator.is_number(token): number_stack.push(token)
            elif Validator.is_operator(token): 
                a = int(number_stack.pop())
                b = int(number_stack.pop())
                result = RPNProcessor.operator_operation_map[token](a, b)
                number_stack.push(result)
        return number_stack.pop()

