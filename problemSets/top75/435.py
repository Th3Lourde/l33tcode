class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        validIntervals = 1
        n = len(intervals)
        lastEnd = intervals[0][1]

        for i in range(1, n):
            s, e = intervals[i]

            if s >= lastEnd:
                validIntervals += 1
                lastEnd = e
            else:
                lastEnd = min(lastEnd, e)

        return n-validIntervals

print(Solution().eraseOverlapIntervals([[1,2],[1,3],[1,4]])) # 2
print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 1
print(Solution().eraseOverlapIntervals([[1,2],[2,3]])) # 0
