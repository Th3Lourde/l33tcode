

class Solution:
    # This is wrong
    def maxProfit(self, prices):
        haveStonk = False
        tmpProfit = 0
        totalProfit = 0

        for i in range(len(prices)-1):
            if haveStonk:
                if prices[i+1] < prices[i]:
                    # Sell

                    tmpProfit += prices[i] - prices[i-1]
                    totalProfit += tmpProfit
                    tmpProfit = 0

                    haveStonk = False

                elif prices[i+1] >= prices[i]:
                    tmpProfit += prices[i] - prices[i-1]

            elif not haveStonk:
                if prices[i+1] > prices[i]:
                    # Buy
                    haveStonk = True
                    # tmpProfit += prices[i]


        return totalProfit




if __name__ == '__main__':
    s = Solution()

    print(s.maxProfit([7,1,5,3,6,4]))
