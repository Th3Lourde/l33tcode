from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals):
        res = cur = 0

        timeArr = []

        for i,j in intervals:
            timeArr.append([i, 1])
            timeArr.append([j, -1])

        timeArr.sort(key=lambda x: (x[0], x[1]))

        for _, action in timeArr:
            cur += action
            res = max(res, cur)

        return res


print(Solution().minMeetingRooms([[26,29],[19,26],[19,28],[4,19],[4,25]]))

print(Solution().minMeetingRooms([[16,20],[14,17],[13,16],[14,16]]))
print(Solution().minMeetingRooms([[1,5], [8,9], [8,9]]))
print(Solution().minMeetingRooms([[13,15],[1,13]]))
print(Solution().minMeetingRooms([[6,15], [13,20], [6,17]]))
