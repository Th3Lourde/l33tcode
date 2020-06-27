'''
Implement the custom stack class

There is a maxSize that the stack can
support.

push, add to top of stack

pop, pop or return -1 if stack is empty

increment, increments the bottom k elements
            of the stack by val

So increment is the only unique thing.
Use a list

Also max size is unique

'''

class CustomStack_list: # Got it right via lists

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []

    def __repr__(self):
        return "{}".format(self.stack)

    def push(self, x):
        if len(self.stack) >= self.maxSize: return
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0: return -1
        return self.stack.pop()

    def increment(self, k, val):
        i = 0

        while i < k and i < len(self.stack):
            self.stack[i] += val
            i += 1


from collections import deque

class CustomStack: # Got it right via lists

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = deque()

    def __repr__(self):
        return "{}".format(self.stack)

    def push(self, x):
        if len(self.stack) >= self.maxSize: return
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0: return -1
        return self.stack.pop()

    def increment(self, k, val):
        i = 0

        while i < k and i < len(self.stack):
            self.stack[i] += val
            i += 1




if __name__ == '__main__':
    stack = CustomStack(5)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.pop()

    stack.increment(2, 7)

    stack
