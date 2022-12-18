'''
Guess there isn't a faster way to do this.

'''

import heapq

class Solution:
    def fillCups(self, amount):
        heap = []
        ans = 0

        for req in amount:
            if req > 0:
                heapq.heappush(heap, -req)

        while heap:
            e1 = heapq.heappop(heap)

            if not heap:
                return ans + -1*e1

            e2 = heapq.heappop(heap)

            print("{}:{}:{}".format(ans, e1, e2))

            ans -= e2
            e1 -= e2

            print("!{}:{}".format(ans, e1))

            if e1 < 0:
                heapq.heappush(heap, e1)

        return ans

'''
ans = 5
[-4, -1]
-3,
'''


print(Solution().fillCups([5,4,4]))
print(Solution().fillCups([1,4,2]))
print(Solution().fillCups([5,0,0]))
