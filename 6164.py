'''
You are given a 0-indexed array nums
that consists of positive ints.

You may choose two indices i,j; i != j,
and the sum of digits of the

So sum the digits of all of the numbers
in the array.

key: sum of digits
value: value of num, maxheap

while len(heap > 2)

pop the two max values, and add them to
ans.




'''

import heapq

class Solution:
    def maximumSum(self, nums):
        d = {}
        ans = -1

        for num in nums:
            key = 0
            numStr = str(num)

            for chr in numStr:
                key += int(chr)

            if key not in d:
                d[key] = [-num]
            else:
                heapq.heappush(d[key], -num)

        # print(d)

        for key in d:
            numList = d[key]

            print(numList)

            while len(numList) >= 2:
                termA = heapq.heappop(numList)
                termB = heapq.heappop(numList)
                # print("{}|{}".format(termA, termB))
                mySum = (termA+termB)*-1
                # print(mySum)
                ans = max(mySum, ans)

        return ans




print(Solution().maximumSum([18,43,36,13,7]))
