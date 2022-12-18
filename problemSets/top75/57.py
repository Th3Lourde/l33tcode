'''
Ok so insert interval. You are given a list of intervals that are sorted.
You are given a new interval.
Add the new interval to the list of sorted intervals.

Adjust the representation of the intervals to filter out any intersections
that occur.

There are many cases to cover:
- The interval that we are given is contained in an interval that already exists in the given list (D)
- There are intervals that exist within the newInterval, and should be removed from the list (D)
- There is an intersection on the left side (D)
- There is an intersection on the right side (D)
- There is no intersection (D)
- The new interval should be appended to the front of the list (D)
- The new interval should be appended to the back of the list (D)
- The given list is empty (D)

Have a second sweep to handle any intersection?

Handle inserting on lists that only have length one

For now, let's just ensure that the new interval is being
inserted in the right place,
then worry about intersections and dealing with them

[[1,5]] | [2,3]
 ^

res = []
i   = 0

'''

# Perform the same level of written analysis for the second solution
# We don't understand the -1, don't use it.

class Solution:
    def insert(self, intervals, I):
        if not intervals:
            return [I]

        res = []

        for i, (l,r) in enumerate(intervals):
            if interval[1] < I[0]:
                resp.append([l,r])
            else:
                if interval[0] > newInterval[1]:
                    return res + [newInterval] + intervals[i:]

                else:
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = min(newInterval[1], interval[1])


        return res + [newInterval]





print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

print(Solution().insert([[3,5],[9,11]], [8,10])) # [[3,5], [8,11]]
print(Solution().insert([[3,5],[9,11]], [5,8])) # [[3, 8], [9,11]]
print(Solution().insert([[3,5],[9,11]], [5,9])) # [[3, 11]]
print(Solution().insert([[3,5],[9,11]], [6,8])) # [[3,5],[6,8],[9,11]]
print(Solution().insert([[3,4],[4,5]], [3,5])) # [[3,5]]
print(Solution().insert([], [1,3])) # [[1,3]]
print(Solution().insert([[2,3]], [0,1])) # [[0,1],[1,3]]
print(Solution().insert([[2,3]], [0,2])) # [[0,3]]
print(Solution().insert([[2,3]], [3,5])) # [[2,5]]
print(Solution().insert([[2,3]], [0,5])) # [[0,5]]
print(Solution().insert([[1,5]], [3,5])) # [[1,5]]
print(Solution().insert([[1,5],[3,10]], [3,5])) # [[1,5],[3,10]]
