import math
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

    function_map = {
        'sin' : lambda a : math.sin(a),
        'cos' : lambda a : math.cos(a),
        'tan' : lambda a : math.tan(a),
        'cot' : lambda a : 1 / math.tan(a)
    }
    
    def evaluate_rpn(self, input):
        number_stack = Stack()
        for token in input:
            if Validator.is_number(token): number_stack.push(token)
            
            elif Validator.is_function(token):
                
                args = []
                for i in range(0, Validator.num_args(token)):
                    args.append(float(number_stack.pop()))
                    
                res = self.function_map[token](*args)
                number_stack.push(res)
            
            elif Validator.is_operator(token): 
                a = float(number_stack.pop())
                b = float(number_stack.pop())
                result = RPNProcessor.operator_operation_map[token](a, b)
                number_stack.push(result)
        
        return number_stack.pop()

