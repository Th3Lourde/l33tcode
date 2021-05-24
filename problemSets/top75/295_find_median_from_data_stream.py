'''
Keep two heaps. Let one heap represent the largest smallest
elements

Let the other heap represent the smallest largest elements

For: 1,2,3

minHeap = [2,1]
maxHeap = [-3]

'''
import heapq
class MedianFinder:
    def __init__(self):
        self.heaps = [],[]

    def addNum(self, num):
        small, large = self.heaps

        heapq.heappush(small, -heapq.heappushpop(large, num))

        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self):
        small, large = self.heaps

        if len(large) > len(small):
            return large[0]

        return (large[0]-small[0]) / 2.0
