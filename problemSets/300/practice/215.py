import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, -1*num)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -1*heapq.heappop(heap)
