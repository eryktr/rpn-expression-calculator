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

    functions_num_params_map = {
            'sin' : 1,
            'cos' : 1,
            'tan' : 1,
            'cot' : 1,
    }

    num_args = lambda token : RPNProcessor.functions_num_params_map[token]

    const_value_map = {
        'e' : math.e,
        'pi' : math.pi
    }

    const_value = lambda const : RPNProcessor.const_value_map[const]
    
    def evaluate_rpn(self, input):
        number_stack = Stack()
        for token in input:
            if Validator.is_number(token): number_stack.push(token)
            
            elif Validator.is_const(token) : number_stack.push(RPNProcessor.const_value(token))

            elif Validator.is_function(token):
                
                args = []
                for i in range(0, RPNProcessor.num_args(token)):
                    args.append(float(number_stack.pop()))
                    
                res = self.function_map[token](*args)
                number_stack.push(res)
            
            elif Validator.is_operator(token): 
                a = float(number_stack.pop())
                b = float(number_stack.pop())
                result = RPNProcessor.operator_operation_map[token](a, b)
                number_stack.push(result)
        
        return number_stack.pop()

