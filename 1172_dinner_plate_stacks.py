'''
So we have an infinite number of stacks arranged in
a row and numbered l-->r from 0.

Each stack has a capacity.

create stacks as we need them.

When we push, we push val to the left most stack
(that has room). I wonder if it would be possible
to keep a pointer with the index of the left most
available stack, and an index on the right most
stack. The answer is probably yes.

we will also need to adjust .l, or .r as we push
and pop elements. Write what we have now and figure
out the rest later.

push:

# push element

self.row[self.l].append(val)

# find the next valid stack

while l < len(self.row) and len(self.row[self.l]) == self.capacity:
    l += 1

if l == len(self.row):
    self.row.append([])

# pop element

if self.row[self.r] == []:
    print("Error")
    return "Error"

# pop the element

r = self.row[self.r].pop()

# find the next valid stack

while r >= 0 and len(self.row[self.r]) == 0:
    r -= 1

if r < 0:
    # reset l, r, rows to [ [] ]
    # this will happen if everything
    # is empty

Would .r ever change after we push
an element?

.r it would change after we push
to a stack that was previously empty.

would we ever need to adjust .l after
popping? If .r < .l and the stack at .r
has room, yes.

Ok so I think that I have push and pop
figured out. Now it's time to do popAtStack

Option 1: index is invalid.

Option 2: index is valid

if the index is left from left,
update left

if the index is right from right
and the stack is not empty, update
right

I think the adjustment from push
will negate the effectiveness of
the .r correction.

Ok I think I got it. Let's run
the test cases on LC.

Made an error, analyze it and
fix the code.

'''

class DinnerPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.row = [ [] ]
        self.l = 0
        self.r = -1

    def __repr__(self):
        return "{}".format(self.row)

    def push(self, val):
        # Assume that .l is valid
        self.row[self.l].append(val)

        # Adjust .l
        while self.l < len(self.row) and len(self.row[self.l]) == self.capacity:
            self.l += 1

        if self.l == len(self.row):
            self.row.append([])

        # Adjust .r if need be
        if self.l > self.r and self.row[self.l] != []:
            self.r = self.l

        elif self.l > self.r and self.row[self.l] == []:
            self.r = self.l - 1

    def pop(self):
        # Assume that .r is valid, unless .r == -1

        if self.r < 0:
            return -1

        # pop if we allowed to
        resp = self.row[self.r].pop()

        # adjust .r
        while self.r >= 0 and len(self.row[self.r]) == 0:
            self.r -= 1

        # adjust .l if need be
        if self.l > self.r and len(self.row[self.r]) < self.capacity:
            self.l = self.r

        if self.l < 0:
            self.l = 0

        return resp

    def popAtStack(self, index):
        if index >= len(self.row) or self.row[index] == []:
            return -1

        resp = self.row[index].pop()

        if index < self.l:
            self.l = index

        if index > self.r and self.row[index] != []:
            print("HI")
            self.r = index

        elif index == self.r and self.row[index] == []:
            while self.row[self.r] == []:
                self.r -= 1

        return resp

if __name__ == '__main__':

    '''
["DinnerPlates","push","push","push","popAtStack","pop","pop"]
[[1],[1],[2],[3],[1],[],[]]

["DinnerPlates","push","push","popAtStack","pop","push","push","pop","pop"]
[[1],[1],[2],[1],[],[1],[2],[],[]]

["DinnerPlates","push","push","popAtStack","popAtStack","push","popAtStack"]
[[1],[1],[2],[0],[1],[3],[0]]
    '''


    dp = DinnerPlates(1)

    dp

    # for i in range(15):
    #     dp.push(i)

    dp.push(1)
    dp.push(2)
    dp.push(3)

    dp.popAtStack(1)

    dp.pop()
    dp.r
    dp.l
