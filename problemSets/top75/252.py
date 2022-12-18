class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x : x[0])

        for idx in range(1, len(intervals)):
            if intervals[idx-1][1] > intervals[idx][0]:
                return False

        return True


print(Solution().canAttendMeetings([[13,15],[1,13]]))
print(Solution().canAttendMeetings([[5,10], [0,30], [15,20]]))
