class Stack:
    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[-1]

    def empty(self):
        return len(self.elements) == 0

    def not_empty(self):
        return not(self.empty())

