'''
Suppose you have N integers from 1 to N.

A beautiful arrangement is an array
constructed by these N numbers that:

the number at the ith position is divisible by i
or:
i is divisible by the number at the ith position

I believe that the array must be of size N

Ok so the goal is to figure out how many times
we can get either of those conditions to be true.


The tricky part is to avoid double counting.
So if we can get something to pass for 1), make
sure that it can't pass for 2), and vice versa.


So we are given n, means we have
an array 1-n.

Upon second thought I think that only
1. or 2. can be true at a time.

Yea so only one can be true at a time,
sick.

So scan for all instances where 1. is true,
scan for all instances where 2. is true.

So a beautiful arrangement satisfies either
1. or 2., for every time that 1. or 2. is true,
we can also vary the order of the rest of the
elements.

So once we have found an element that satisfies 1 or 2,
we must take into account the ways we can vary the rest
of the elements.

Once we have found a beaut,

mult by (n-1)! ← For permutations

Given a number, is 1) or 2) true?

Figure out which num is divisible by which i
Figure out which i is divisible by num

Loop through nums.

How to figure out what numbers our number is
divisible by, brute force?

loop through all terms in n, see if divisible.

def isBeautiful(num, N):
    n = 1
    ans = 0

    while n <= num:
        if num % n:
            ans += 1

        elif n % num:
            ans += 1

        n += 1

    return ans




ans = 0

for i in range(1, N+1):
    ans += isBeautiful(i, N)

return ans * (N-1)

Ok so there is some double counting going
on, how can I get rid of that?

Not sure, because we ran the code, I like
the idea of dividing by two, or N.

Let's try N and see what happens.

No dice, so maybe we should actually create the
different arrangements in a set.

This is a bit different then dynamic programming,
as we are not using previous queries to solve our
future problems.

So my guess is to store all of the arrangements that
I have seen so far.

However I'm guessing that we shouldn't be doing this,
because last time we didn't store any of the things that
we have done thus far.

I'm guessing that we start with holding one value the way
it is, then adding in other things.

e.g. N == 5

[1,2,3,4,5]

Brute force, go through all possible permutations,
if a permutation is beautiful, add to ans.

If it isn't, continue.

So how could we do this?

We can start with everything in the original order,
which is one.

Then we can unfreeze one term (which does nothing)

Then unfreeze three terms and switch them around
and put things in a set.add

Then unfreeze four terms and switch them around
and put things in a set.

Let's just look at the answer, learn what the approach
is, and learn.

'''



import math

class Solution:

    def countArrangement(self, N):

        def f(n, arr, e):
            if e == n+1: return 1
            a = 0

            for i in range(len(arr)):
                                    # In this circumstance our arr is indexed at 1.
                if arr[i] == 0 and (e%(i+1) == 0 or (i+1)%e == 0):
                    # We have found a placement for element e
                    arr[i] = 1
                    a += f(n, arr, e+1) # Place the next element
                    arr[i] = 0

            return a

        return f(N, [0 for i in range(N)], 1)



    def countArrangement_1(self, N):
        ans = 0

        def isBeautiful(num, N):
            n = 1
            a = 0

                # Case 1
            while n <= num:
                if num % n == 0:
                    a += 1

                n += 1

            while n <= N:
                if n % num == 0:
                    a += 1

                n += 1

            return a

        for i in range(1, N+1):
            ans += isBeautiful(i, N)

        return math.floor((ans * (N-1))/(N))


if __name__ == '__main__':
    s = Solution()

    print(s.countArrangement(5))

    '''
    1 → 1
    2 → 2
    3 → 3
    4 → 8
    5 → 10
    6 → 36


    '''
