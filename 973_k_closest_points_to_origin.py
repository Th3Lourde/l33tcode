'''

'''

import heapq
import math

class Solution:
    def kClosest(self, points, k):
        heap = []
        for l,r in points:
            heapq.heappush(heap, (math.sqrt(l**2 + r**2), l,r) )

        response = []

        for _ in range(k):
            dist, l, r = heapq.heappop(heap)
            response.append([l,r])

        return response



print(Solution().kClosest([[1,3],[-2,2]], 1))
print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
