'''
Given the array nums, for each nums[i] find out how many numbers
in the array are smaller than it. That is, for each nums[i] you
have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

We would like to return an array, where arr[i] is the number of
elements in nums that is smaller than nums[i].

Ok so let's start by talking about an example.

[8,1,2,2,3]
[4,0,1,1,3]

What we could do is:
loop through list, find min, find max,
sort the list <-- Maybe sort the list, then get min,max

All elements \in [0, 100].

have a mapping between unique elements and their index in the answer.

[8,1,2,2,3] ← nums
[         ]

mapping = {}

for i in range(len(nums)):
    e = nums[i]
    if e in mapping:
        mapping[e].append(i)

    elif e not in mapping:
        mapping[e] = [i]

mapping = { 8:[0], 1:[1], 2:[2,3], 3:[4] } <-- We might not need this, we can just use
                                            nums to lookup the element that we want.

numLT = {} ← lookup element, get number of elements less than it

Ok so we really want to create a mapping ∋ we can lookup and element
and get the number of elements lt it.

So how can we create that mapping?

So the mapping could be a list of 100 long.

mapping = [0]*101  #[0, 100] for numbers we support, indices 0 ⭃ 101

loop through nums, for every num, add one to all indices less than element.

loop through nums again, index the mapping, create answer based upon this mapping.

[8,1,2,2,3]

mapping = [0,...,0] # len(mapping) == 101

After looping:
mapping = [0,0,1,2,]

Ok so it isn't good enough to just add one every time.

Sort the list, loop through the list, if our element is not a dup,
set the mapping = number elements before our current num.

[8,1,2,2,3] → [1,2,2,3,8]

1 → 0
2 → 1
3 → 3 len(numsSorted[:i])
8 → 4

When we create the mapping, this mapping will actually be our answer?
No, we need to return with the order preserved.

Make sure to check that we ignore duplicates : )

Sort : 0(nlog(n))
Create Mapping : 0(n)
Create Answer : 0(#unique elements)

space complexity: # unique elements, (depending on if we count the return value as memory)

We cannot use a monotonically decreasing stack, as we do not care about the orientation
of the elements, just their values.




'''

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        numsS = list(nums)
        numsS.sort()
        mapping = {}

        mapping[numsS[0]] = 0

        for i in range(1, len(numsS)):
            if numsS[i] != numsS[i-1]:
                mapping[numsS[i]] = len(numsS[:i])

        ans = []

        for e in nums:
            ans.append(mapping[e])

        return ans

if __name__ == '__main__':
    s = Solution()

    # [4, 0, 1, 1, 3]
    print(s.smallerNumbersThanCurrent([8,1,2,2,3]))

    # [2,1,0,3]
    print(s.smallerNumbersThanCurrent([6,5,4,8]))

    # [0,0,0,0]
    print(s.smallerNumbersThanCurrent([7,7,7,7]))
