'''
Given a list of non-negative numbers,
arrange them such that they form the largest number and return it

We can use a min heap:

(1,0), (2)

put all the numbers in as tuples, then just pop and
'''

import heapq
from collections import deque

class Solution:
    def largestNumber(self, nums):
        heap = []

        ans = []

        for n in nums:
            q = deque()
            tmpN = n

            while tmpN:

                if tmpN % 10 == 0:
                    q.appendleft(float('inf'))
                else:
                    q.appendleft(-1 * (tmpN % 10))

                tmpN //= 10

            q.append(n)

            heapq.heappush(heap, tuple(q))

        # print(heap)

        while heap:
            e = heapq.heappop(heap)
            # print("{}|{}".format(e, e[-1]))
            # print("{}|{}".format(e, str(e[-1])))
            ans.append(str(e[-1]))
            # ans = ans + str(e[-1])

        # return ans
        return "".join(ans)



print(Solution().largestNumber([3,30,34,5,9]))

print(Solution().largestNumber([10,2]))

a = (1,2,3,123)
a[-1]

a = []

for i in range(1, 50):
    a.append(i)

a
