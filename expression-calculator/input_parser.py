from stack import Stack
from validator import Validator
class InputParser:        
    
    def fix_lacking_spaces(self, input):
        exp = input
        for operator in Validator.priorities:
            exp = exp.replace(operator, " " + operator + " ")
        for var in Validator.variables:
            exp = exp.replace(var, " " + var + " ")
        
        return exp

    def trim(self, input):
        return input.replace(' ', '')

    def add_implicit_operators(self, input : str):
        exp = input
        for var in Validator.variables:
            exp = exp.replace(var, "*"+var+"*")
            for operator in Validator.priorities:
                if operator != '(' and operator != ')' : 
                    exp = exp.replace('*'+operator, operator)
                    exp = exp.replace(operator + '*', operator)
        if exp.startswith('*') : exp = exp[1:]
        if exp.endswith('*') : exp = exp[:-1]
        return exp

    def to_rpn(self, input):
        remove_empty_strings = lambda  tokens : [x for x in tokens if x != ""]
        tokens = self.trim(input)
        tokens = self.add_implicit_operators(tokens)
        tokens = self.fix_lacking_spaces(tokens)
        tokens = remove_empty_strings(tokens.split(' '))
        operator_stack = Stack()
        output = []
        head_priority = lambda : Validator.priority(operator_stack.top())


        for token in tokens:
            if not(Validator.is_legal(token)) : raise ValueError()
            
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
                        while not(operator_stack.empty()) and  head_priority() >= this_priority : output.append(operator_stack.pop())
                        operator_stack.push(token)
        
        while not(operator_stack.empty()): output.append(operator_stack.pop())        
        
        return output