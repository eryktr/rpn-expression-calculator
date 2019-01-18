class Stack:
    def __init__(self):
        self.elements = []
        self.push = lambda self, value : self.elements.append(value)
        self.pop = lambda self : self.elements.pop()
        self.top = lambda self : self.elements[-1]
        
        
        