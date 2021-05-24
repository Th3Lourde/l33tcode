import heapq
class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = -1
            else:
                freq[n] -= 1

        heap = []

        for key in freq:
            heapq.heappush(heap, (freq[key], key))

        kMostFrequent = []

        for i in range(k):
            freq, element = heapq.heappop(heap)
            kMostFrequent.append(element)

        return kMostFrequent

print(Solution().topKFrequent([1,1,1,2,2,3], 3))
