import heapq

class Solution:
    def topKFrequent(self, nums, k):
        num_to_freq = {}

        for n in nums:
            if n not in num_to_freq:
                num_to_freq[n] = 1
            else:
                num_to_freq[n] += 1

        heap = []

        for num in num_to_freq:
            heapq.heappush(heap, (-1*num_to_freq[num], num))

        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


print(Solution().topKFrequent([1,1,1,2,2,3],2))
