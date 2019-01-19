from stack import Stack
from validator import Validator
class InputParser:        
    
    def to_rpn(self, input):
        remove_empty_strings = lambda  tokens : [x for x in tokens if x != ""]
        
        tokens = remove_empty_strings(input.split(' '))
        operator_stack = Stack()
        output = []
        head_priority = lambda : Validator.priority(operator_stack.top())

        for token in tokens:
            if not(Validator.is_legal(token)) : return "Illegal token"
            if Validator.is_number(token): output.append(token)
            
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