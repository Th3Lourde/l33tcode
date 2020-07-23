
'''
A pair (i,j) is good if:
    - i < j
    - nums[i] == nums[j]

Return the number of good pairs

Niave Solution:
0(n²) → For every element, cycle through
        the list and identify all good pairs

Less-Niave Solution:
First pass, create a dictionary, value : index <-- keep the list sorted
For every element, look-up the value in the dictionary.
    All of the indices right of the index of the value are "good pairs"
    So add the number of elements right of the current element that we
    are looking at.

[1,2,3,1,1,3]

Pass 1: Dict

{1: [0,3,4], 2: [1], 3:[2,3]}

We could even have a set of elements whose value has more than one
elements in it. Sure we can do that.

'Pass' 2: Get ans

So we have three elements in 1, # of good pairs is:

(0,3)
(0,4)
(3,4)

I wonder, if given the number of times an element occurs,
if we can return the number of good pairs?

5 | 4 + 3 + 2 + 1

So factorial only we sum instead of multiply?

[1,1,1,1] == 4

3 + 2 + 1. Cool. So how can we do this easily with math?

For a sequence of numbers 1→n, formula: ((n)(n+1))/(n)

We start at n+1,

So given a length of n, sum (n-1)(n)/(n-1) ?

3*4 == 12/3 == 4

I am high-confidence that this works.

So, create the dict, create a set of elements
that have > 1 element in the list.

The itr through the set, apply math formula to len(arr),
and then return.

n+1 C 2

(n+1)(n)/2


'''
import math

class Solution:
    def numIdenticalPairs(self, nums):
        ans = 0
        mapping = {}
        itr = set()

        for i in range(len(nums)):

            if nums[i] not in mapping:
                mapping[nums[i]] = [i]

            elif nums[i] in mapping and len(mapping[nums[i]]) == 1:
                mapping[nums[i]].append(i)
                itr.add(nums[i])

            elif nums[i] in mapping and len(mapping[nums[i]]) > 1:
                mapping[nums[i]].append(i)

        for i in itr:
            n = len(mapping[i])-1
            ans += int((n*(n+1))/2)


        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.numIdenticalPairs([1,2,3,1,1,3]))
    print(s.numIdenticalPairs([1,1,1,1]))
    print(s.numIdenticalPairs([1,2,3]))

    print(s.numIdenticalPairs([1,3,2,1,3,2]))
