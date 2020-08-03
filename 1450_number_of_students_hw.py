'''
Ok we are given three inputs.

There are students studying in the libary.
Students must sign in and sign out of the libary.

Given a queryTime, return the number of students
in the library at that time.

Ok so here is what I am thinking:


pointer starts at startTimes <= queryTime.
If the endTime <= queryTime, ans += 1

Since startTime might not be sorted, it makes
sense for us to loop through all of the data
that we have been given.

'''

class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        ans = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1

        return ans
