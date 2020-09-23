
'''
Given an array of integers,
find the max length of a subarray where
the product of all its elements is positive.

A subarray is an array of consecutive elements

zero is a valid answer.

Naive answer is 0(n²) brute-force.

Keep two counters, length and valid.

If the product is valid, ans = max(ans, length)

Is product is not valid, continue

Every time we see a -1, toggle valid.

If we make product valid, update length

Let's only keep valid. Length can be generated via idx's

If we always start at the beginning, we will miss things.

if we vary where we start, we won't run into this issue: 0(n²)

So perform the valid/invalid toggle for every element.

ans = 0

if valid and nums[i] != -1:
    # update ans
    ...

elif not valid and nums[i] == -1:
    # update ans
    ...

if nums[i] == -1:
    valid = not valid


return ans

Ok so answer correct, however TLE.

So what can we do here?

We can split by 0. We kinda already do that, as
we break whenever we see a zero.

One loop through the list, every time we see two
-1's, replace them with 1's.

1 -1 -1 -1 1

1 1 1 -1 1

1 -1 -1 -1 1 1

1 -1 -1 -1 1 1

Every time we see a negative, throw idx into stack.
I feel like this is a dp problem.

Because every time you decide to include or not include
a -1, you make a choice.

Um, we could split the array into smaller arrays by the location
of a zero.

Start with the assumption that the entire subarray is valid,
go through all subarrays of a certain size, if number of -1's
is even return ans?

Ok so let's try this problem again.

remove the zeros, then what? Well we will have a choice about
The negative that we don't use, (if we have an odd number of negs)

We can get rid of the lhs neg, or the rhs neg.

Ok so let's do the zero thing first

So split by zeroes.

Every time we see a zero, put the lhs
of the list into another list.

e.g. [1,2,3,0,4,5,6]
            ^

[1,2,3,0,4,5,6] ← arr = arr[i+1:]

[[1,2,3], ]




'''

class Solution:

    def getMaxLen(self, nums):

        def splitByZero(arr):
            i = 0
            subs = []

            while i < len(arr):
                if arr[i] == 0:

                    sub = arr[:i]

                    if sub != [0]:
                        subs.append(sub)

                    arr = arr[i+1:]
                    i = -1

                i += 1

            if arr != [0]:
                subs.append(arr)

            return subs

        itrs = splitByZero(list(nums))

        ans = 0

        for itr in itrs:
            lN = None
            rN = None
            numNegs = 0

            for idx in range(len(itr)):
                if itr[idx] < 0:
                    if lN == None:
                        lN = idx
                    rN = idx
                    numNegs += 1

            if numNegs % 2 == 0:
                tmpAns = len(itr)

            elif numNegs % 2 != 0:
                # [1, -1, -1, -1, 1]
                #
                # remove left neg
                tmpAns = max(lN, len(itr)-lN-1)
                # remove right neg
                tmpAns = max(tmpAns, rN, len(itr)-rN-1)
                print("For: {} tmpAns: {}".format(itr, tmpAns))

            ans = max(ans, tmpAns)

        return ans











    def getMaxLen_1(self, nums):
        ans = 0

        for start in range(len(nums)):
            tmp = 0
            valid = True

            for i in range(start, len(nums)):

                if nums[i] == 0:
                    break

                if valid and nums[i] > 0 or not valid and nums[i] < 0:
                    tmp = i-start+1

                if nums[i] < 0:
                    valid = not valid

            ans = max(ans, tmp)

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.getMaxLen([0,0,0,0,0]))

    print(s.getMaxLen([-4,0,0,-9,-10]))


    print(s.getMaxLen([0,1,-2,-3,-4]))
    print(s.getMaxLen([1,1,-2,-3,-4]))
    print(s.getMaxLen([-4, 1,1,-2,-3]))



    print(s.getMaxLen([1,2,3,0,3,2,1,0,1,2,3,0,1,2,3]))
    print(s.getMaxLen([1,2,3,0,3,2,1,0,1,2,3,0,1,2,3,0]))

    print(s.getMaxLen([1,-2,-3,4]))
    print(s.getMaxLen([0,1,-2,-3,-4]))
    print(s.getMaxLen([-1,-2,-3,0,1]))
    print(s.getMaxLen([-1,2]))
    print(s.getMaxLen([1,2,3,5,-6,4,0,10]))


    print(s.getMaxLen([1,2,3,5,-6,-4,0,10,-1]))
    print(s.getMaxLen([1,2,3,5,-6,4,0,10,-1]))
    print(s.getMaxLen([1,2,3,5,-6,4,1,10,-1]))

    print(s.getMaxLen([0,0,-1,0]))
    print(s.getMaxLen([0,0,0,0]))
    print(s.getMaxLen([0,1,0,0]))
    print(s.getMaxLen([1,0,0,0]))
    print(s.getMaxLen([0,0,1,0]))
    print(s.getMaxLen([0,0,0,1]))
    print(s.getMaxLen())
