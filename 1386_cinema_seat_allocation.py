'''
What are the valid locations to put people?

1 2 3 | 4 5 6 7 | 8 9 10
  x     x   x

So only check 2,4,6

'''
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        d = defaultdict(set)

        for row,col in reservedSeats:
            d[row].add(col)

        ans = (n - len(d))*2

        # print(d.values())
        # For all rows that don't have any seats reserved, can reserve two seats
        # print((n - len(d))*2)

        for row in d.values():
            if not {2,3,4,5,6,7,8,9} & row:
                ans += 2
            elif (not {2,3,4,5} & row) or (not {4,5,6,7} & row) or (not {6,7,8,9} & row):
                ans += 1

        return ans



s = Solution()

print(s.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])) # 4
print(s.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]])) # 2
print(s.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]])) # 4
