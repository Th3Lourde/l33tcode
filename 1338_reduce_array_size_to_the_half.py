'''
We are given an array of integers.

You can choose a set of integers and
remove all of the occurrences of these
integers in the array.

The goal is to pick a set of integers such
that the size of the array, after removal,
decreases by at least 50%.

The goal is also to select a size that is
of as small of a size as possible.

How could we do this?

Well we could create a dictionary that
would record the number of occurrences
that each integer has.

We could then sort and step through the
elements of max frequency, subtracting
the number of times their element occurs
in our list, until the list has less than
50% of its size.


So one pass in order to create the dict.
nlog(n) to sort things

At max, 0(n) to find our answer.

Maybe, instead of using a dict, we could
use a list[[int, int]] and sort via lambda
value?

Create dict. Get values, sort the values,
subtract the values until we are done.

Since we don't know how many values we will
need to keep track of, we will have to sort
the vals










'''
import math

class Solution:
    def minSetSize(self, arr):
        d = {}

        for e in arr:
            if e in d:
                d[e] += 1

            else:
                d[e] = 1

        vals = list(d.values())

        vals.sort()

        ans = 0

        targ = math.ceil(len(arr)/2)
        current = len(arr)

        while current > targ:
            current -= vals.pop()
            ans += 1

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
