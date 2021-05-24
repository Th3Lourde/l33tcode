class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        localMin = prices[0]

        for i in range(len(prices)):
            if prices[i] < localMin:
                localMin = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i]-localMin)

        return maxProfit

s = Solution()

print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
