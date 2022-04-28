'''
The next greater element of some element x in an array is the first greater element
that is to the right of x in the same array

For each index i in nums 1, find the index j such that nums1[i] == nums2[j] and determine
the next greater element of nums2[j] in nums2.

If there is no greater element, the answer for this query is -1.

Lets start with nums2. For every element in nums2, we'll need to answer the question of:
- Is there an element to the right of this element that is greater than this element?

Not sure if we can optimize this. What we can do, however, is create a dictionary
so the look-up in nums2 can be quick.

max = 4

nums2: [1,2,3,4]
                e

stack = [4]
d = {1: 2, 2:3, 3:4}
'''

class Solution:

    # 0(len(nums1)*len(nums2))
    def nextGreaterElement_1(self, nums1, nums2):
        d = {}

        for idx in range(len(nums2)):
            d[nums2[idx]] = idx

        resp = []

        for _, num in enumerate(nums1):
            greater = -1

            i = d[num]

            while i < len(nums2):
                if nums2[i] > num:
                    greater = nums2[i]
                    break

                i += 1

            resp.append(greater)

        return resp

    def nextGreaterElement(self, nums1, nums2):
        d = {}
        stack = []

        for e in nums2:

            while stack and stack[-1] < e:
                greater = stack.pop()
                d[greater] = e

            stack.append(e)

        return [d.get(n, -1) for n in nums1]


print(Solution().nextGreaterElement( [4,1,2], [1,3,4,2] ))
print(Solution().nextGreaterElement([2,4], [1,2,3,4]))
