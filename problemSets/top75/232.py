'''
Ok make a queue using stacks

[6,5,4]
[2,3]

The issue is that we can't get the elements at the bottom of the
stack.

I can only use push, peek, pop, empty.
The issue is how to perform pop.

Ok so let's have two stacks.
The first stack is used for pushing too
The second stack is used for popping

push:
- appendleft to stack1

pop:
- if len(stack2) > 0, pop from stack1
- else pop all elements from stack2 to stack one then pop from stack2

peek:
- if len(stack2)
    - return top of stack2
- else pop/append elements to stack2 and return the top

empty;
- len(stack1), len(stack2) is empty

[3,2,1]
[1,2,3]

'''

from collections import deque

class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x):
        self.s1.append(x)

    def reverse(self):
        while self.s1:
            self.s2.append(self.s1.pop())

    def pop(self):
        if not self.s2:
            self.reverse()

        return self.s2.pop()

    def peek(self):
        if not self.s2:
            self.reverse()

        return self.s2[-1]


    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0


q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

q.pop()
q.peek()
q.empty()

q.s1
q.s2
