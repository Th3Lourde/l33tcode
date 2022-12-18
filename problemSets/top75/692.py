import heapq

class Solution:
    def topKFrequent(self, words, k):
        d = {}
        heap = []
        ans = []

        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1


        for word in d:
            heapq.heappush(heap, (-1*d[word], word))

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans

print(Solution().topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
