'''
Given integers a, b

Return their sum without using
+.

When you add you do two things:
Addition without carrying
Carrying

how can we get addition without carrying?

If the values are both one put zero
Else, put the value (or 1)

1100
1010
----
0110

And: If both are 1, put 1, else put 0
Or: If either are 1, put 1, else put 0
xor: x ^ y | if bit in y is 0, put whatever is in x. Else put what is the complement in x

Ok so addition without carry is x ^ y
How do we get the carries?

A carry will only occur when they are both 1
So x & b
'''

a = 9
b = 10

bin(a)
bin(b)

bin(a^b)
bin((a&b) << 1)
bin(a+b)

bin(-20)

if bin(-20) < bin(0): print("hi")

class Solution:
    def getSum(self, a, b):
        mask = 0xffffffff

        while b:
            sumNoCarry = (a^b) & mask
            carryNoSum = ((a&b) << 1) & mask
            a,b = sumNoCarry, carryNoSum

        if (a >> 31)&1:
            return ~(a^mask)

        return a



    def getSum_1(self, a, b):
        print("A: {}".format(a))
        print("B: {}".format(b))

        mask = 0xffffffff

        while b:
            sumNoCarry = (a^b) & mask
            carryNoSum = ((a&b) << 1) & mask
            a,b = sumNoCarry, carryNoSum

        # if a < 0:
        #     print("Negative")
        print(a)
        print(a>>31)
        # If we go right 31 bits and
        # still have a bit left, we know
        # that we have a negative #
        if (a>>31) & 1:
            ~(a^mask)

        return a

print(Solution().getSum(-10,-1))

bin(9)
bin((-9 >> 50)&1)
