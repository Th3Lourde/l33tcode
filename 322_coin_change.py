import sys
sys.path[0] = "/home/th3lourde/Documents/InterviewPrep/tools/python"

'''
[186,419,83,408]
6249
20

So the question is really whether or not these numbers can divide another number evenly.
How can we go about this?

One way to do this is to iterate through all possible permutations of these elements and
see if you can reduce this number down to zero.

lcd(a,b): the smallest number that can be expressed as a multiple of a and b
|--> Meaning a^n = b^y = lcd(a,b), y,n \in Z.
gcd(a, b): largest number (not zero) that divides a and b

So apparently this is a dynamic programming problem.

So how would I do this?
Let's say that we have [a,b,c,d] and target sum z
start with a, reduce z via z // a. Pick an element from [b,c,d]. Rinse and repeat until
we are out of coins. If we can do it, return the number of coins. If we can't, return None

I'm assuming that we use up all of the coins. We won't need to do this.


'''

from priorityQueue.priorityQueueF import priorityQueue

class Solution:

    def coinChange(self, coins, amount): # Not doing DP atm. Make progress on your list :)
        def perms(coin, coins, num, amount):
            # Account for the number of coins we can use.

            num += amount // coins[coin]
            amount = amount % coins[coin]

            coins = list(coins)
            del coins[coins[coin]]

            if amount == 0: return coins

            ans = None

            for c in range(len(coins)):
                r = perms(c, list(coins), num, amount)
                if r:
                    if ans == None:
                        ans = r
                    else:
                        ans = min(r, ans)


            return ans



    def coinChange_1(self, coins, amount): # Doesn't work. I think that I should be using lcd or gcd or something similar
        pq = priorityQueue('max', coins)

        ans = 0

        while pq.getSize() != 0:
            coin = pq.poll()
            ans += amount // coin
            amount = amount % coin

            if amount == 0:
                return ans

        return -1



if __name__ == '__main__':
    s = Solution()

    print(s.coinChange([2], 3))
