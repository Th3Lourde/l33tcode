class Solution:
    def deleteAndEarn(self, nums):
        dict = {}

        for n in nums:
            if n not in dict:
                dict[n] = n
            else:
                dict[n] += n

        houses = list(dict.keys())
        houses.sort()

        if len(houses) == 0:
            return 0
        elif len(houses) == 1:
            return houses[0]

        dp = [dict[houses[0]], dict[houses[1]]] + [0 for _ in range(len(houses)-2)]

        if houses[0]+1 != houses[1]:
            dp[1] += dp[0]

        for i in range(2, len(houses)):
            if houses[i-1]+1 == houses[i]:
                dp[i] = max(dp[i-1], dp[i-2]+dict[houses[i]])
                if i > 2:
                    dp[i] = max(dp[i], dp[i-3]+dict[houses[i]])
            else:
                dp[i] = max(dp[i-1]+dict[houses[i]], dp[i-2]+dict[houses[i]])

        # print("dict:{}|houses:{}".format(dict, houses))
        # print(dp)

        return max(dp[-1], dp[-2])






s = Solution()

print(s.deleteAndEarn([1,1,1,2,4,5,5,5,6])) # 18

print(s.deleteAndEarn([3,4,2])) # 6
print(s.deleteAndEarn([2,2,3,3,3,4])) # 9
print(s.deleteAndEarn([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4])) # 61
