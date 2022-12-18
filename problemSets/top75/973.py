'''
Maintain a heap where the distance is the value that is
used to position the point in heap.

After all points are put into the (min) heap,
pop k times and return the remaining points
'''

import heapq
import math

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x,y in points:
            heapq.heappush(heap, (math.sqrt(x**2 + y**2), [x,y]))

        ans = []

        for _ in range(k):
            _, point = heapq.heappop(heap)
            ans.append(point)

        return ans

print(Solution().kClosest([[1,3],[-2,2]], 1))
