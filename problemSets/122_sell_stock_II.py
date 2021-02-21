'''
[7,1,5,3,6,4]
           ^

min = 4
max = 4
p = 7

if max-min > 0:
    p = max-min

[1,2,3,4,5]
         ^

min = 1
max = 5
p = 0


'''



class Solution:
    def maxProfit(self, prices):
        if len(prices) < 1: return 0

        minPrice = prices[0]
        maxPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > maxPrice:
                maxPrice = prices[i]

            elif prices[i] < maxPrice:
                localProfit = maxPrice-minPrice

                if localProfit > 0:
                    profit += localProfit

                minPrice, maxPrice = prices[i], prices[i]

        localProfit = maxPrice-minPrice

        if localProfit > 0:
            profit += localProfit

        return profit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))
