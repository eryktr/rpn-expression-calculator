class Stack:
    def __init__(self):
        self.elements = []
    
    push = lambda self, value : self.elements.append(value)
    pop = lambda self: self.elements.pop()
    top = lambda self: self.elements[-1]
    empty = lambda self: len(self.elements) == 0
    not_empty = lambda self : not(self.empty())
        