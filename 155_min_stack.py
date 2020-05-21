


class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, x):
        self.stack.append(x)

        if len(self.minStack) == 0:
            self.minStack.append(x)

        elif len(self.minStack) != 0:
            self.minStack.append(min(self.minStack[-1], x))

    def pop(self):
        self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.minStack[-1]





class MinStack_1:
    def __init__(self):
        self.min_val = []
        self.data = []

    def push(self, x: int) -> None:
        if (len(self.data) == 0):
            self.data.append(x)
            self.min_val.append(x)

        elif (len(self.data) != 0):
            self.data.insert(0, x)

            if (self.min_val[0] >= x):
                self.min_val.insert(0, x)

    def pop(self) -> None:
        # return value from top of stack and
        # remove from stack
        if (len(self.data) == 0):
            return None
        elif (len(self.data) > 0):
            val = self.data[0]
            if (val == self.min_val[0]):
                self.min_val.remove(self.min_val[0])
                self.data.remove(self.data[0])
                return val

            elif (val != self.min_val[0]):
                self.data.remove(self.data[0])
                return val

    def top(self) -> int:
        # return top value, no remove
        return self.data[0]

    def getMin(self) -> int:
        # return the minimum value in stack
        return self.min_val[0]


    def __str__(self):
        return "Data: {} \n Min: {}".format(self.data, self.min_val)




if __name__ == '__main__':
    minStack = MinStack()

    minStack.push(0)
    minStack.push(1)
    minStack.push(0)

    print(minStack)


    r = minStack.getMin()
    print(r)

    minStack.pop()
    r = minStack.top()
    print(r)
    r = minStack.getMin()
    print(r)
