import bisect
import heapq
import math
import collections
import sortedcontainers
class MKAverage:

    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.q = collections.deque([])
        self.slist = sortedcontainers.SortedList()

    def addElement(self, num):
        self.q.append(num)
        self.slist.add(num)

        if len(self.q) > self.m:
            lru = self.q.popleft()
            self.slist.remove(lru)


    def calculateMKAverage(self):
        if len(self.q) < self.m:
            return -1

        return math.floor(sum(self.slist[self.k:-self.k])/(self.m-self.k*2))


mk = MKAverage(3, 1)
mk.addElement(3)
mk.addElement(1)
mk.calculateMKAverage() # -1
mk.addElement(10)
mk.calculateMKAverage() # 3
mk.addElement(5)
mk.addElement(5)
mk.addElement(5)
mk.calculateMKAverage() # 5
