'''
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        arr1 = nums1[0:m]
        idx1 = 0
        idx2 = 0
        writeIdx = 0

        while idx1 < m and idx2 < n:
            if arr1[idx1] <= nums2[idx2]:
                nums1[writeIdx] = arr1[idx1]
                idx1 += 1
            else:
                nums1[writeIdx] = nums2[idx2]
                idx2 += 1

            writeIdx += 1

        while idx1 < m:
            nums1[writeIdx] = arr1[idx1]
            writeIdx += 1
            idx1 += 1

        while idx2 < n:
            nums1[writeIdx] = nums2[idx2]
            writeIdx += 1
            idx2 += 1

        return nums1

print(Solution().merge([0], 0, [1], 1 ))
print(Solution().merge([1], 1, [], 0 ))
print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3 ))
