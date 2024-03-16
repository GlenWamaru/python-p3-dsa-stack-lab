class Stack:

    def __init__(self, items = [], limit = 100):
        self.stack = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.full():
            raise Exception("Stack is full")
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

    def full(self):
        return len(self.stack) == self.limit

    def search(self, target):
        try:
            index = self.stack.index(target)
            return len(self.stack) - index - 1
        except ValueError:
            return -1
