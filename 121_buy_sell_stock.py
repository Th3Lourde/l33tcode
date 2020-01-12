'''
Stocks will either go up, down, or stay the same (which never really happens)

Identify local mins and local maxes: make sure stock doesn't stay the same


a max is only valid if the stock decreases the next day

find all indices that represent valid mins and maxes

a min is valid if there is a max that we can sell at and profit

so start by finding all maxes that we can profit after

if prices[i] > prices[i+1] --> valid max

after we find all valid maxes, search for a min for every max

We would sell at that max



'''





class Solution:

    def maxProfit_elegent(self, prices):

        if len(prices) < 2:
            return 0

        minP = [] # minP[i] returns min(prices[:i])
        currentMin = prices[0]
        currentMax = prices[1]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < currentMin:
                currentMin = prices[i]
            minP.append(currentMin)

            if prices[i] - minP[i] > profit:
                profit = prices[i] - minP[i]

        print(minP)
        return profit


    # brute-force, works, too slow
    def maxProfit_brute(self, prices):
        if len(prices) < 2:
            return 0

        max = prices[1]-prices[0]

        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if prices[j]-prices[i] > max:
                    max = prices[j]-prices[i]


        if max < 0:
            return 0

        return max

    # Works, not as efficient as could be
    def maxProfit_2(self, prices):

        # Testing assumption that you can only buy/sell once
        '''
        index of min < index of max
        '''
        maxes = []
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                maxes.append([i, prices[i]])

        profit = 0

        for j in range(len(maxes)):
            end = maxes[j][0]

            proxyMin = min(prices[:end])

            if maxes[j][1]-proxyMin > profit:
                profit = maxes[j][1]-proxyMin

        return profit






        # maxes = {}
        # for i in range(1, len(prices)-1):
        #     if prices[i] > prices[i+1]:
        #         # [index, value]
        #         # maxes.append([i, prices[i]])
        #         maxes[i] = prices[i]
        #
        # print("prices: {}".format(prices))
        # print("maxes: {}".format(maxes))








    # This is wrong
    def maxProfit_1(self, prices):
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
