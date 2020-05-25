
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __repr__(self):
        return "s1: {} s2: {}".format(self.s1, self.s2)

    def push(self, x):

        while self.s1 != []:
            element = self.s1.pop()
            self.s2.append(element)

        self.s1.append(x)

        while self.s2 != []:
            element = self.s2.pop()
            self.s1.append(element)


    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return len(self.s1) == 0


q = MyQueue()

q.push(1)
print(q)

q.push(2)
print(q)

q.push(3)
print(q)

print(q.pop())
print(q)

print(q.pop())
print(q)

print(q.pop())
print(q)
