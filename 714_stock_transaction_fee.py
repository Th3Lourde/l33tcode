class Solution:
    # Top-Down, too slow
    def maxProfit_1(self, prices, fee):
        dp = [-1 for _ in range(len(prices))]

        def itr(dp, idx):
            if idx >= len(prices):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            minV = prices[idx]
            max_p = 0
            idxs = []
            # If we are still here, prices[idx] represents the first
            # point at which, without fee, there is profit

            for i in range(idx, len(prices)):
                if prices[i] <= minV:
                    minV = prices[i]
                    idxs.append(i)
                elif prices[i]-minV-fee > 0:
                    max_p = max(max_p, prices[i]-minV-fee +  itr(dp, i))

            for i in idxs:
                dp[i] = max_p

            return max_p

        return itr(dp, 0)

    def maxProfit(self, prices, fee):
        if len(prices) < 2:
            return 0

        holding = [0 for _ in range(len(prices))]
        sold = [0 for _ in range(len(prices))]
        holding[0] = -prices[0]-fee

        for i in range(1, len(prices)):
            # keep holding or buy at prices[i]
            holding[i] = max(holding[i-1], sold[i-1]-prices[i]-fee)
            sold[i] = max(sold[i-1], holding[i-1]+prices[i])

        return sold[-1]








s = Solution()
print(s.maxProfit([1,3,2,8,4,9], 2))
print(s.maxProfit([1,3,7,5,10,3], 3))

print(s.maxProfit([4,5,2,4,3,3,1,2,5,4], 1))

'''
So we can instead try a state machine

So what are the different states that we can have?

We are in a state where we can buy a stock, or we are
in a state where we can sell as stock.

We go from buying stock to selling stock via -= (stockPrice + penalty)
at initial purchase.

From go from being able to sell a stock to being able to buy a stock
using profit += stock[i]

[1,3,7,5,10,3] | 3
          ^
Ok so looks like we maintain two arrays, each detailing our profit

let's pay the price when we buy the stock, then keep

So we are figuring out what the max profit is. For every stock we are
finding the max value for buy or the max value for sell.

buy[0]=-price[0]-fee

buy[i] = max(buy[i-1], sell[i-1] - price[i] - fee)
sell[i] = max(sell[i-1], buy[i-1]+price)


'''
