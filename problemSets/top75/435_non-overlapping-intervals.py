class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        termsToRemove = 0
        minL = intervals[0][0]
        minR = intervals[0][1]

        for l,r in intervals[1:]:
            # if minL <= l < minR:
            if l < minR:
                if r < minR:
                    minR = r

                termsToRemove += 1
            else:
                minL = l
                minR = r

        return termsToRemove

print(Solution().eraseOverlapIntervals([])) # 0
print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 1
print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
print(Solution().eraseOverlapIntervals([[1,2],[2,3]])) # 2
print(Solution().eraseOverlapIntervals([[1,3],[1,2],[2,5],[2,3],[2,4],[3,4]])) # 3

print(Solution().eraseOverlapIntervals([[1,3],[0,2],[1,4],[1,5],[2,3],[3,4],[1,3]])) # 4


print(Solution().eraseOverlapIntervals([[0,7],[1,2],[1,4],[2,3],[3,4],[4,5]])) # 4
