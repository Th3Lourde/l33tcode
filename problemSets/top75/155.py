class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

        self.stack.append(val)

    def pop(self):
        self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
