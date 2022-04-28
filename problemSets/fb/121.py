'''
You are given an array prices where prices[i]
is the price of a given stock on the ith day.

You can buy and sell a stock once.
Figure out the max profit you can acrue

[7,1,5,3,6,4]
           ^

buyPrice = 1
profit = 5

Buy a stock, if you find the stock for a lower
price, buy it then.

If you find a higher price, simulate how much
money you would make if you sold then.



'''

class Solution:
    def maxProfit(self, prices):
        buyPrice = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            else:
                profit = max(profit, prices[i]-buyPrice)

        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit( [7,6,4,3,1]))
print(Solution().maxProfit( [3,2,1,5]))
