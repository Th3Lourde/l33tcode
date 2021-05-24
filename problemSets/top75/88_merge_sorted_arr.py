'''
p <= q ?

[1,2,3,0,0] | nums1
       p

[2,5,6]     | nums2
       q

[1,2,2,3,5,6]

'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        mergedArr = []
        p = 0
        q = 0

        while p+q < m+n:
            if p >= m:
                for i in range(q, n):
                    mergedArr.append(nums2[i])
                break

            if q >= n:
                for i in range(p, m):
                    mergedArr.append(nums1[i])
                break

            if nums1[p] < nums2[q]:
                mergedArr.append(nums1[p])
                p += 1
            else:
                mergedArr.append(nums2[q])
                q += 1

        for i in range(len(nums1)):
            nums1[i] = mergedArr[i]

        return nums1

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
