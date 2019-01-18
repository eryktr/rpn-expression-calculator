from stack import Stack
class InputParser:
    def __init__(self):
        self.priorities = {
            '+' : 1,
            '-' : 1,
            '*' : 2,
            '/' : 2,
            '%' : 2,
            '^' : 3
        }
    priority = lambda self, value : self.priorities[value]

    
    def to_rpn(self, input):
        remove_empty_strings = lambda  tokens : [x for x in tokens if x != ""]
        is_operator = lambda token : self.priorities[token] != None
        is_legal = lambda  token : is_number(token) or is_operator(token)
        def is_number(token):
            try: int(token); return True
            except: return False

        tokens = remove_empty_strings(input.split(' '))
        operator_stack = Stack()
        output = []
        head_priority = lambda : self.priority(operator_stack.top())

        for token in tokens:
            if is_number(token): output.append(token)
            elif is_operator(token):
                if operator_stack.empty():
                     operator_stack.push(token)      
                else:
                    this_priority = self.priority(token)
                    if this_priority > head_priority() : operator_stack.push(token)
                    else:
                        while not(operator_stack.empty()) and  head_priority() >= this_priority : output.append(operator_stack.pop())
                        operator_stack.push(token)
            
        while not(operator_stack.empty()): output.append(operator_stack.pop())        
        
        return output

p = InputParser()
r = p.to_rpn("1 + 2 * 3 + 3 ^ 4")
print(r)