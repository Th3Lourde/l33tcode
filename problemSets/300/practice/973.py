import math
import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        def calc_distance(x,y):
            return math.sqrt(x**2+y**2)

        for x,y in points:
            dist = calc_distance(x,y)

            heapq.heappush(heap, (-dist, [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)

        resp = []

        for _ in range(k):
            _, point = heapq.heappop(heap)
            resp.append(point)

        return resp

print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
print(Solution().kClosest([[1,3],[-2,2]], 1))
