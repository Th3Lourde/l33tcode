'''
You have a set that contains all positive integers [1,2,3,4,...]

We have a class to implement.

init --> initializes obj to contain all positive integers
popSmallest --> remove and return the smallest integer
addBack --> adds a positive integer back to the infinite set, if not already present

So let's have a heap
and a pointer

the pointer will contain the smallest integer that has never been popped.
we will also have a heap where we will put the integers that we are adding back.

the procedure for popSmallest is as follows:
- check heap, if heap empty, return k, k+=1
- if heap not empty, return pop from heap

addBack
- push to the heap
- we will have a min heap, so popSmallest will work fine.

k=1


'''

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.k = 1
        self.heap = []
        self.heapSet = set()

    def popSmallest(self):
        if self.heap:
            ret = heapq.heappop(self.heap)
            self.heapSet.remove(ret)
            return ret

        resp = self.k
        self.k += 1
        return resp

    def addBack(self, num):
        if num < self.k and num not in self.heapSet:
            self.heapSet.add(num)
            heapq.heappush(self.heap, num)


obj = SmallestInfiniteSet()

obj.addBack(1)
obj.popSmallest()

print(obj.k)
print(obj.heap)
