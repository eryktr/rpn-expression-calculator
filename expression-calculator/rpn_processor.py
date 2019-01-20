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
        'sin' :  [lambda a : math.sin(a), 1],
        'cos' :  [lambda a : math.cos(a), 1],
        'tan' :  [lambda a : math.cos(a), 1],
        'cot' :  [lambda a : 1/math.tan(a), 1],
        'log' :  [lambda a : math.log(a), 1],
        'asin' : [lambda a : math.asin(a), 1],
        'acos' : [lambda a : math.acos(a), 1],
        'atan' : [lambda a : math.atan(a), 1],
        'sinh' : [lambda a :math.sinh(a), 1],
        'cosh' : [lambda a :math.cosh(a), 1],
        'tanh' : [lambda a :math.tanh(a), 1],
        'abs' :  [lambda a : -a if a < 0 else a, 1]
    }
    
    num_args = lambda token : RPNProcessor.function_map[token][1]

    const_value_map = {
        'e' : math.e,
        'pi' : math.pi
    }

    const_value = lambda const : RPNProcessor.const_value_map[const]
    
    def evaluate_rpn(self, input, value=0):
        def pop_args(stack, token):
            args = []
            for i in range(0, RPNProcessor.num_args(token)):
                args.append(float(stack.pop()))
            return args

        def evaluate_function(token, args):
            return  self.function_map[token][0](*args)

        def evaluate_operator(stack, token):
            a = float(stack.pop())
            b = float(stack.pop())
            result = RPNProcessor.operator_operation_map[token](a, b)
            return result

        number_stack = Stack()
        for token in input:
            if Validator.is_number(token): number_stack.push(token)
            
            elif Validator.is_const(token) : number_stack.push(RPNProcessor.const_value(token))
            elif Validator.is_variable(token) : number_stack.push(value)
            
            elif Validator.is_function(token):    
                args = pop_args(number_stack, token)
                res = evaluate_function(token, args)
                number_stack.push(res)
            
            elif Validator.is_operator(token): 
                result = evaluate_operator(number_stack, token)
                number_stack.push(result)
        
        return number_stack.pop()