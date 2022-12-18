'''
You are given two pos int arrs:
- nums
- numsDivide

You can delete any number of elements from nums.

Return the min number of deletions s.t. the smallest
element in nums divides all the elements in numsDivide

So delete from nums until the smallest element
in nums divides all the elements of numsDivide.

if not possible, return -1


so have a heap for nums
counter of deletes
remove duplicates in numsDivide

'''

import heapq

class Solution:
    def minOperations(self, nums, numsDivide):
        d = {}
        heap = []
        dels = 0
        numsDivide.sort(reverse=True)

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for key in d:
            heapq.heappush(heap, (key, d[key]))

        while heap:
            val, freq = heapq.heappop(heap)
            divis = True

            for num in numsDivide:
                if num%val != 0:
                    divis = False
                    break

            if divis:
                return dels

            dels += freq

        return -1

print(Solution().minOperations([4,3,6],[8,2,6,10] ))
print(Solution().minOperations([2,3,2,4,3],[9,6,9,3,15] ))
