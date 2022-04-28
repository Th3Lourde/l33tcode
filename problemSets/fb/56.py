'''
Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all of the intervals in the input.

[1,3],[2,6],[8,10],[15,18]
 l
   r
        i

if l <= i[0] <= r:
    r = max(r, i[1])

Every time this case is triggered, we are merging


[
[]

]

'''

class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = []

        l = intervals[0][0]
        r = intervals[0][1]

        for i in range(1, len(intervals)):
            if l <= intervals[i][0] <= r:
                r = max(r, intervals[i][1])
            else:
                merged.append([l,r])
                l = intervals[i][0]
                r = intervals[i][1]

        merged.append([l,r])

        return merged

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,3],[2,6], [1,4], [1,9],[8,10],[15,18]]))
