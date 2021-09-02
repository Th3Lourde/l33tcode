'''
So when we are adding what are we doing?
We are doing two things.

The first thing that we are doing is getting the digit
for every value after adding. Another is carrying the value to the
next place if need-be.

So how can we do this?
Well these are all binary numbers so that isn't too bad.

0
1

The value of the one's place will be determined by an and
operator.

But how do we know whether or not to carry a one?

If both digits are 1's then we do.

1) How do we get sum without carry
2) How do we get carry without sum

10101010101010
11100011001100

1 ^ 1 --> 0
0 ^ 1 --> 1
1 ^ 0 --> 1
0 ^ 0 --> 0

1 & 1 --> 1
0 & 1 --> 0
1 & 0 --> 0
0 & 0 --> 0

Ok so then how do we take this result and combine them?

Well we can't directly add them. Let's look an an example

4 --> 100
5 --> 101
9 --> 1001

4^5
100^101
100
101
= 001 (carry no sum)

100&101
100
101
= 100 (sum no carry)

However we want the ones place to go right one so:

(100&101) << 1
= 010

However this isn't our answer.

If we continue recursively:
= 001 (carry no sum)
= 010 (sum no carry)

001 ^ 010
001
010
=011

001 & 010
001
010
=000

We get our answer.






'''

class Solution:
    # Fails for -1, 1
    def getSum_1(self, a, b):
        if b == 0: return a
        return self.getSum(a^b, (a&b) << 1)

    def getSum(self, a, b):
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

print(Solution().getSum(4,5))
print(Solution().getSum(5,5))
print(Solution().getSum(5,0))
print(Solution().getSum(0,5))
print(Solution().getSum(-1,1))
