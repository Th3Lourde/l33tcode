'''
Given two numbers
- hours
- minutes

return the smaller of the two angles
that those hands form

15/90 --> 3/18

Ok so find the difference between minutes
and hour

or hour and minutes

take the smaller of these two and multipley the diff by 3/18
return that

also need to convert the hour to minutes

[2,7,11,15]

(n)+(n-1)+(n-2)+...




'''

class Solution:
    def angleClock(self, hour, minutes):
        # minToAngle = 1/60
        minToAngle = 90/15
        # minConst = 3/18

        if hour == 12:
            hour = 0

        hour = (hour)*5 + 5 * (minutes/60)

        # print("Hour: {}".format(hour))
        # print("Minutes: {}".format(minutes))

        minDiff = abs(hour-minutes)

        if hour > 30 and minutes < 30:
            minDiff = min(minDiff, (60-hour)+minutes)
        elif hour < 30 and minutes > 30:
            minDiff = min(minDiff, (60-minutes)+hour)


        # print("MinDiff: {}".format(minDiff))

        return minDiff*minToAngle

print(Solution().angleClock(1, 57))

print(Solution().angleClock(12, 30))
print(Solution().angleClock(3, 30))
print(Solution().angleClock(3, 15))
