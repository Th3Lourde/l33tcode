'''
Given an integer array nums, and k
return the kth largest element

So naive solution is to use a heap

How to do this better is to have a
sub array length k, add the element
to it if len < k

Else, if element > smallest element, use
bisect left to figure out where to put it,
remove the smallest element


'''

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)

        return heapq.heappop(heap)

print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
