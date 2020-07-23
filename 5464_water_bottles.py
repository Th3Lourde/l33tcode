'''
You are given water bottles, they have water.

You drink all of them.

You can exchange empty water bottles for full water bottles.

The exchange rate is numExchange.

Given that you are going to maximize the number of water bottles
that you could possibly drink, how many water bottles will you
end up being able to drink?

given n empty bottles, return num of full bottles you get.

n // exchangeRate

ans = 0

while numBottle > 0:
    ans += numBottles

    numBottles = numBottles // exchangeRate

return ans

False assumption: you lose the bottles that
you have already drank.

'''

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        full = numBottles
        empty = 0
        ans = 0

        while full > 0:
            ans += full

            empty += full
            full = 0

            full = empty // numExchange

            empty -= full * numExchange

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.numWaterBottles(9, 3))

    print(s.numWaterBottles(15, 4))

    print(s.numWaterBottles(5, 5))

    print(s.numWaterBottles(2, 3))
