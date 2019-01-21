from stack import Stack
from validator import Validator
class InputParser:        
    
    def __fix_lacking_spaces(self, input):
        exp = input
        for operator in Validator.priorities:
            exp = exp.replace(operator, " " + operator + " ")
        for var in Validator.variables:
            exp = exp.replace(var, " " + var + " ")
        
        return exp

    def __trim(self, input : str):
        return input.replace(' ', '')

    def __add_implicit_operators(self, input : str):
        def __add_in_variables(exp : str):
            ex = exp
            for var in Validator.variables:
                ex = ex.replace(var, "*"+var+"*")
            return ex
        
        def __add_in_constants(exp : str):
            ex = exp
            for const in Validator.constants:
                ex = ex.replace(const, '*'+const+'*')
            return ex

        def __add_in_functions(exp : str):
            ex = exp
            for func in Validator.functions:
                ex = ex.replace(func, "*" + func)
            return ex
        
        def __fix_improper_operators(exp : str):
            ex = exp
            ex = exp.replace(")(", ")*(")
            for operator in Validator.priorities:
                if operator != '(' and operator != ')' : 
                    ex = ex.replace('*'+operator, operator)
                    ex = ex.replace(operator + '*', operator)
            ex = ex.replace('(*', '(')
            ex = ex.replace('*)', ')')
            if ex.startswith('*') : ex = ex[1:]
            if ex.endswith('*') : ex = ex[:-1]
            for i in range (0,10):
                ex = ex.replace(str(i)+"(", str(i)+"*(")
            return ex
        
        exp = input
        exp = __add_in_variables(exp)
        exp = __add_in_constants(exp)
        exp = __add_in_functions(exp)
        exp = __fix_improper_operators(exp)
        
        return exp

    __remove_empty_strings = lambda  self, tokens : [x for x in tokens if x != ""]

    def __tokenize(self, input): 
        tokens = self.__trim(input)
        tokens = self.__add_implicit_operators(tokens)
        tokens = self.__fix_lacking_spaces(tokens)
        tokens = self.__remove_empty_strings(tokens.split(' '))
        return tokens

    def to_rpn(self, input):
        tokens = self.__tokenize(input)
        operator_stack = Stack()
        output = []
        head_priority = lambda : Validator.priority(operator_stack.top())


        for token in tokens:
            if Validator.is_illegal(token) : raise ValueError()
            
            if Validator.is_numeric(token): output.append(token)
            
            elif Validator.is_function(token):
                operator_stack.push(token)
            
            elif Validator.is_operator(token):
                if Validator.is_open_brace(token) : operator_stack.push(token)
                
                elif Validator.is_close_brace(token):
                    while operator_stack.top() != '(': output.append(operator_stack.pop())
                    operator_stack.pop()
                
                elif operator_stack.empty():
                     operator_stack.push(token)      
                
                else:
                    this_priority = Validator.priority(token)
                    if this_priority > head_priority() : operator_stack.push(token)
                    else:
                        while operator_stack.not_empty() and  head_priority() >= this_priority : output.append(operator_stack.pop())
                        operator_stack.push(token)
        
        while operator_stack.not_empty(): output.append(operator_stack.pop())        
        
        return output