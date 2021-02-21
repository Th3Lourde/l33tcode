'''
Given integer array nums.

ith bag contains nums[i] balls

Given operation and max number of times you can perform
the operation.

Operation:
Take any bag of balls and divide it into two new bags with
a positive number of balls

Perform the operation with the goal of minimizing the max value
of
'''

import heapq as h

class Solution:
    def minimumSize(self, nums, maxOperations):
        heap = []

        for num in nums:
            h.heappush(heap, -1*num)

        while maxOperations > 0:
            maxOperations -= 1

            e = heap.heappop()

            if e % 2 == 0:
                h.heappush(heap, e//2)
                h.heappush(heap, e//2)
            else:
                h.heappush(heap, e//2)
                h.heappush(heap, e//2+1)

        return h.heappop()
