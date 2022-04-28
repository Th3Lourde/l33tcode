import heapq

class Solution:
    # Too slow
    def findKthNumber_1(self, m, n, k):
        heap = []

        for r in range(1, m+1):
            for c in range(1, n+1):
                # Have a min heap
                heapq.heappush(heap, r*c)

        return heapq.nsmallest(k, heap)[-1]

    # Ok so I got the brute force solution down
    # I don't think that this algo works
    # Turns out this is a binary search problem
   # def findKthNumber_1(self, m, n, k):
   #      if k == 1:
   #          return 1
   #
   #      count = 1
   #      starting = (1,1)
   #      row = True
   #
   #      while starting != (m,n):
   #          if count == k:
   #              return starting[0]*starting[1]
   #
   #          movingR = starting[0]
   #          movingC = starting[1]
   #
   #          while movingC < m or movingR < n:
   #              if row:
   #                  if movingC < m:
   #                      movingC += 1
   #                      count += 1
   #                      # print(starting[0]*movingC)
   #
   #                      if count == k:
   #                          return starting[0]*movingC
   #
   #                  row = False
   #
   #              elif not row:
   #                  if movingR < n:
   #                      movingR += 1
   #                      count += 1
   #
   #                      if count == k:
   #                          return starting[1]*movingR
   #
   #                  # print(starting[1]*movingR)
   #
   #                  row = True
   #
   #          starting = (min(starting[0]+1, m), min(starting[1]+1, n))
   #          count += 1

class Solution:
    def findKthNumber(self, m, n, k):
        def enough(x):
            return sum([min(x // i, n) for i in range(1, m+1)]) >= k
        l, r = 1, m*n

        while l < r:
            mid = (l+r)//2

            if not enough(mid):
                l = mid+1

            else:
                r = mid

        return l
class Solution:
    def findKthNumber(self, m, n, k):
        def lessEq(x):
            return sum([min(x//i, n) for i in range(1, m+1)]) >= k

        beg, end = 1, m*n
        while beg < end:
            mid = (beg + end)//2
            if not lessEq(mid):
                beg = mid + 1
            else:
                end = mid
        return beg









for k in range(1,81):
    print(Solution().findKthNumber(9,9,k))
