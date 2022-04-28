from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.ave = 0
        self.q = deque()

    def next(self, val):
        if len(self.q) < self.size:
            self.q.appendleft(val)

            ave = 0

            for val in self.q:
                ave += val/len(self.q)

            self.ave = ave

        else:
            oldVal = self.q.pop()
            self.q.appendleft(val)

            self.ave -= oldVal/self.size
            self.ave += val/self.size

        return self.ave


ma = MovingAverage(3)
ma.next(1)
ma.next(10)
ma.next(3)
ma.next(5)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
