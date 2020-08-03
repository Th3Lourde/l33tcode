'''
Given an array of integers, some of the elements
appear once, other elements appear twice.

∀ e ∈ arr[int], e ∈ [1, len(arr[int])]

Find all elements that appear twice in the array

Niave, make a dict, if frequency goes above 1, add
the element to an arr[int], return arr. Easy money.

Or, for every element see if it appears again in the
list, 0(n²), easy money x 2

However, neither of these are 0(n), 0(c)

sum 1+2+...+n = ((n+1)(n))/2

Given: [4,3,2,7,8,2,3,1]
len() == 8

So sum should be 8*7/2 = 56/2 = 28

28

Loop through each element, subtract the value

4: 24
3: 21
2: 19
7: 12
8: 4
2: 2
3: -1
1: -2

28 - x - y + z + w = -2

seen = set()
ans = []

for num in nums:
    if num in seen:
        ans.append(num)

    elif num not in seen:
        seen.add(num)

return ans

Ok so I think that I have it.

Loop through list. Since we know that
the elements must exist in [1,n], we
can calculate the index at which any
given element must exist at (if we were
to sort it).

If we look at the element at the target
index, and it is the same as the element that we have,
add it to our arr[int]

Then set the current index to None.

Loop through list, swapping elements until they are in
the right location. If we see a repeat, setting the current
index that we are at to None.

Return the arr[int] when done.



'''


class Solution:
    def findDuplicates(self, nums):
        seen = set()
        ans = []

        for num in nums:
            if num in seen:
                ans.append(num)

            elif num not in seen:
                seen.add(num)

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.findDuplicates([4,3,2,7,8,2,3,1]))

    print(s.findDuplicates([1,2]))
