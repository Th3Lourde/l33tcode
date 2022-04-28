'''
[1,8],[2,6],[8,10],[15,18], [18,19], [21,22]
                                      ^

lBound = 15
rBound = 19

ans = [[1,10], [15,19]]

'''

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda intervals: intervals[0])

        ans = []

        lBound, rBound = intervals[0][0], intervals[0][1]

        for idx in range(1, len(intervals)):
            if rBound < intervals[idx][0]:
                ans.append([lBound, rBound])
                lBound, rBound = intervals[idx][0], intervals[idx][1]

            else:
                rBound = max(rBound, intervals[idx][1])

        ans.append([lBound, rBound])

        return ans

print(Solution().merge([[1,4],[0,4]]))

print(Solution().merge([[1,8],[2,6],[8,10],[15,18],[18,19],[21,22]]))
