'''
Given an array, rotate the array to the right by k steps
where k is non-negative.

We could create a new arr with the values in the new places
However it's probably preferred to update the array in-place

We should also mod k to the length of the array


Input:
 0 1 2 3 4 5 6
[1,2,3,4,5,6,7] | k = 3
 5 6 7 1 2 3 4
 ^

tmp = 5

[5,6,7,1,2,3,4]

So the question is how many times do we need to do this?
In this case we only needed to do it once.

However there are probably cases where we need to do it more
than that.

I think it is based upon the length of the array and the k value

length = 5
k = 3
Rotations = 3

length = 5
k = 2
Rotations = 2

length = 5
k = 1
Rotations = 1

length = 5
k = 4
Rotations = 2


012345 | k = 3
012012

012345 | k = 2
010101

012345 | k = 1
000000

012345 | k = 4
010101

There's probably some math trick that we can do,
however I don't know it.

Ok so I was thinking about it wrong, it's a bit difficult
to do the simulation, I'm happy that I stopped.

If we just move each element right once, but then do it k-times,
we'll be good.

012345
------
^
tmp = 0

Ok so I was right the first time.
This is actually 0(n^2)

How can we do this in a linear path?

k % len(nums)


nums[j + i], nums[len(nums) - k + i]
nums[3+1], nums[6-3+1]
nums[4], nums[4] = nums[3], nums[3]

345012 | k = 3

tmp = 1
swaps = 4

So keep track of the number of swaps that we make
Else, just make a swap the k elements and then move on

312045 | k = 3
    n

tmp = 1
start = 1
next = 4
swapsLeft = 4

'''

class Solution:
    def rotate_1(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        def rotateRight():
            tmp = nums[0]

            for i in range(len(nums)-1):
                tmp, nums[i+1] = nums[i+1], tmp

            nums[0] = tmp

        for _ in range(k):
            rotateRight()

    def rotate(self, nums, k):
        swapsLeft = len(nums)
        idx = 0
        n = len(nums)

        while swapsLeft > 0:
            tmp = nums[idx]
            start = idx
            next = (idx+k) % n

            while next != start:
                nums[next], tmp = tmp, nums[next]
                next = (next+k) % n

                swapsLeft -= 1

            nums[start] = tmp
            swapsLeft -= 1

            idx += 1

        return nums

'''
[1,2,3,4] | 2
swapsLeft = 4
idx = 0
n = 4

tmp = -1
start = 0
next = 3

nums[3], -1 = -1, nums[3]
'''

print(Solution().rotate([1,2,3,4,5,6,7], 2))
print(Solution().rotate([1,2,3,4], 2))
print(Solution().rotate([-1,-100,3,99], 2))
