'''

capacity = 10
[1,2,3,4,5,6,7,8,9,10]
 -------
         -
           -
             -
               -
                 -
                   -
                   ^

days = 6
running_sum = 10
'''


class Solution:
    def shipWithinDays(self, weights, days):
        def daysGivenCapacity(capacity):
            days = 0
            running_sum = 0

            for weight in weights:
                if running_sum + weight > capacity:
                    days += 1
                    running_sum = 0

                running_sum += weight

            if running_sum > 0:
                days += 1

            return days

        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l+r) // 2

            if daysGivenCapacity(m) > days:
                l = m + 1
            else:
                r = m

        return l

print(Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
