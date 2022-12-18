'''
You are given an array of prices
prices[i] is the price of the stock on day i
You can buy and sell the stock once.

What is the maximum profit that you can take home?

Keep track of the min.
Every time we see a price that is > than current stock
record the profit

Every time we see a price lower than what we have, update lower price

profit = 4
minPrice = 1

[7,1,5,3,6,4]
     ^
'''

class Solution:
    def maxProfit(self, prices):
        profit = 0
        minPrice = float('inf')

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = max(profit, price-minPrice)

        return profit

print(Solution().maxProfit([7,6,4,3,1]))
