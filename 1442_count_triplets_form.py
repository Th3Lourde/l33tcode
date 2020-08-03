'''
Ok let's learn that bitwise operator.

Ok so the prompt is to countTriplets that can
form two arrays of equal XOR.

What is XOR?

XOR returns true when both of the inputs given are
unique.

So basically, we want to know whether or not all
of the elements ∈ [i,j-1] are unique and then
whether or not elements ∈ [j,k] are unique.

Well the question isn't really whether or not the
elements are unique, but whether or not both subarrays
output the same value when we pass XOR operation through
all of the elements.

I wonder what a good way to do this might be.

What we could do is use a set that we remove and add elements
to.

Set wouldn't work, that would only tell us what the elements are.

We could check whether or not the size of the sets are the same
as the length of the subarray.

One of the major assumptions that we are making is how XOR operates
when one of the elements match.

The current assumption is that if at least one element matches, the
result is the same when 1-n elements match.

We are assuming the question is more along the lines of: are the subarrays
that we form composed of only unique elements?

We should probably check this assumption.

Ok so this assumption holds iff we are working 1 and 0. Else it doesn't
really match what is true.

Let's look at the discussion for this one and move on :)

Ok so here is what someone else does:

We compute the ^ in a smart way that allows us to minimize
the number of computations. My answer is correct, and it
has more operations then it needs to have.

So we have these two subarrays that we are creating.

The first thing that we do is define what starting points
we are going to iterate through.

We start at 0 and end up at len(arr)-1

For each starting point, we have a few ending points that we
can cycle through.

Yea no. Let's move on. I'd rather not have fun with bitwise
operations atm.







'''

# Pretty sure that this is write. Got TLE. Probably has to do
# with this bitwise operator trick that I don't know.
# Should probably learn it ♡

class Solution:
    def countTriplets(self, arr):

        def validTrpl(tpl):
            a = arr[tpl[0]]
            b = arr[tpl[1]]

            for i in range(tpl[0]+1, tpl[1]):
                a ^= arr[i]

            for j in range(tpl[1]+1, tpl[2]+1):
                b ^= arr[j]

            return a == b

        ans = 0

        for i in range(0, len(arr)-1):
            k = len(arr)-1

            while i+1 <= k:
                j = i+1

                while j <= k:
                    trpl = (i,j,k)

                    if validTrpl(trpl):
                        ans += 1

                    j += 1

                k -= 1

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.countTriplets([2,3,1,6,7]))
    print(s.countTriplets([1,1,1,1,1]))
    print(s.countTriplets([2,3]))
    print(s.countTriplets([1,3,5,7,9]))
    print(s.countTriplets([7,11,12,9,5,2,7,17,22]))
