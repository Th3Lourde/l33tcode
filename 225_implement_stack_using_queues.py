'''
Implement a stack with the following
operations, with a queue.

so we can only insert from the
left,
pop from the right

push a
push b
push c

[c, b, a]

pop, can only pop from rhs.
so put everything into another
queue and return the last element
instead of adding it to the queue

set the new queue to our queue

top can look at the first element
in the queue q[0] is ok.

'''

from collections import deque

class MyStack_list: # This works
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return "{}".format(self.queue)

    def push(self, x):
        self.queue.insert(0, x)

    def pop(self):

        if self.empty(): return

        newQueue = []

        while True:
            term = self.queue.pop()

            if self.queue:
                newQueue.insert(0, term)
            else:
                break

        self.queue = newQueue

        return term


    def top(self):
        if self.empty(): return

        return self.queue[0]


    def empty(self):
        return len(self.queue) == 0


class MyStack: # Using dequeue
    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        return "{}".format(self.queue)

    def push(self, x):
        self.queue.appendleft(x)
        # self.queue.insert(0, x)

    def pop(self):

        if self.empty(): return

        newQueue = deque()

        while True:
            term = self.queue.pop()

            if self.queue:
                newQueue.appendleft(term)
            else:
                break

        self.queue = newQueue

        return term


    def top(self):
        if self.empty(): return

        return self.queue[0]


    def empty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    s = MyStack()

    s.push("c")
    s.push("b")
    s.push("a")

    s

    s.pop()

    s.top()

    s.empty()
