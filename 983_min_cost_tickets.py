'''
Skip all days that aren't travel days,
or just copy what the last day was.

dp = [0 for _ in range(days[-1]+1)]
dp[1] = cost[0]

# Create a set of biz days, so we know when
# we need to buy and when we don't

for i in range(2, len(dp)):
    if i not in travelDays:
        dp[i] = dp[i-1]
    else:
        if i-1 > 0:
            dp[i] = dp[i-1]+costs[0]

        if i-7 > 0 and dp[i-7] + costs[1] < dp[i]:
            dp[i] = dp[i-7]+costs[1]

        if i-30 > 0 and dp[i-30] + costs[2] < dp[i]:
            dp[i] = dp[i-30]+costs[2]

return dp[-1]




[1,4,6,7,8,20] | [2,7,15]
         ^



20-1 = 19, cost 9+2
20-7 = 13, cost 9+7


1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
2 2 2 4 4 6 8 9 9 9  9  9  9  9  9  9  9  9  9  0





[1,2,3,4,5,6,7,8,9,10,30,31] | [2,7,15]
                         ^

31 - 1 = 30, cost 15+2
31 - 7 = 24, cost 13+7
31 - 30 = 1, cost 2+15 = 17


- 1 2 3 4 5  6  7  8 9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
0 2 4 6 8 10 12 14 9 11 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 15 0


'''

class Solution:
    def mincostTickets(self, days, costs):
        travelDays = set()

        for day in days:
            travelDays.add(day)

        dp = [0 for _ in range(days[-1]+1)]
        dp[days[0]] = costs[0]

        for i in range(days[0], len(dp)):
            if i not in travelDays:
                dp[i] = dp[i-1]
            else:
                if i-1 >= 0:
                    dp[i] = dp[i-1]+costs[0]
                else:
                    dp[i] = costs[0]

                if i-7 >= 0 and (dp[i-7] + costs[1]) < dp[i]:
                    dp[i] = dp[i-7]+costs[1]

                elif i-7 < 0 and costs[1] < dp[i]:
                    dp[i] = costs[1]

                if i-30 >= 0 and (dp[i-30] + costs[2]) < dp[i]:
                    dp[i] = dp[i-30]+costs[2]

                elif i-30 < 0 and costs[2] < dp[i]:
                    dp[i] = costs[2]

        # print(dp)

        return dp[-1]

s = Solution()




print(s.mincostTickets([1,4,6,7,8,20], [7,2,15])) # 6

print(s.mincostTickets([6,8,9,18,20,21,23,25], [2,10,41])) # 16

print(s.mincostTickets([1,4,6,7,8,20], [2,7,15])) # 11
print(s.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])) # 17
