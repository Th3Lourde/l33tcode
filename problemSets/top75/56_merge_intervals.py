class Solution:
    def merge(self, intervals):
        if not intervals:
            return []


        intervals.sort(key=lambda x: x[0])

        idx = 0
        mergedIntervals = [intervals[0]]

        for l,r in intervals[1:]:
            if mergedIntervals[idx][0] <= l <= mergedIntervals[idx][1] and mergedIntervals[idx][1] < r:
                mergedIntervals[idx][1] = r

            elif mergedIntervals[idx][1] < l:
                mergedIntervals.append([l,r])
                idx += 1

        return mergedIntervals

print(Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))

print(Solution().merge([[1,4],[1,5]]))

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,4],[2,4],[3,4]]))
