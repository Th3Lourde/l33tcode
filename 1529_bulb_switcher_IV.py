
'''
There is a room with n bulbs.
The bulbs are numbered [0, n-1]
arranged in a row left to right

Initially, all bulbs are turned off.

Goal is to get bulb configuration to be
the same as target.

In order to do this, we can flip bulbs.

If we want to flip the bulb positioned
as idx i, we would flip all bulbs from i → n-1
(again these are indices).

10111
00000 → 00111

00111 → 00111

Interesting. We could start flipping from the lhs,
however that probably wouldn't give us the min number
of flips.

We could test both sides? Unless we know for sure that
one strat will always be better than the other.

10101

I actually think that they are the same.

Starting from the LHS feels a bit easier.

We can either create it or just grok the pattern (let's grok it)

val = 1 → Val represents the value upon seeing we 'swap'

We count the number of times we change the value, return that

Got it, easy money.

'''

class Solution:
    def minFlips(self, target):
        # if True, swapping on ones
        # if False, swapping on zeroes
        targ = '1'
        ans = 0

        def swapTarg(targ):
            if targ == "1":
                return "0"

            elif targ == "0":
                return "1"

        for t in target:
            if t == targ:
                ans += 1

                targ = swapTarg(targ)

        return ans


if __name__ == '__main__':
    s = Solution()

    s.minFlips("101")
    s.minFlips("00000")
    s.minFlips("001011101")

    s.minFlips("")
