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
