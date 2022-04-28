import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, -1*num)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -1*heapq.heappop(heap)

print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
