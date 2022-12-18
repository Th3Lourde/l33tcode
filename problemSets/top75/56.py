class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        ans = []
        n = len(intervals)
        l = 0

        while l < n:
            termL, termR = intervals[l]

            r = l+1

            while r < n and termL <= intervals[r][0] <= termR:
                termR = max(termR, intervals[r][1])
                r += 1

            ans.append([termL, termR])
            l = r

        return ans


print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
