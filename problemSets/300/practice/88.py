'''
nums1 is sorted
nums2 is sorted

sort both nums1 and nums2 and return the output
in nums1

one way of doing this is to move all of the elements in nums1 everytime
an element from nums2 should go there. This is linear time.

A better way to do it would be to create a copy of nums 1
and then use a 2 pointer approach to put the elements into
nums1 in a sorted fashion

[1,2,2,3,5,6]
           ^

n1    = [1,2,3]
               ^

nums2 = [2,5,6]
             ^
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        n1 = list(nums1)
        ptr1 = 0
        ptr2 = 0
        ansIdx = 0

        while ptr1 < m and ptr2 < len(nums2):
            if n1[ptr1] < nums2[ptr2]:
                nums1[ansIdx] = n1[ptr1]
                ptr1 += 1
            else:
                nums1[ansIdx] = nums2[ptr2]
                ptr2 += 1

            ansIdx += 1

        while ptr1 < m:
            nums1[ansIdx] = n1[ptr1]
            ptr1 += 1
            ansIdx += 1

        while ptr2 < len(nums2):
            nums1[ansIdx] = nums2[ptr2]
            ptr2 += 1
            ansIdx += 1

        # return nums1

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
