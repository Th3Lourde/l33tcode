import heapq
class Solution:
    def minOperations(self, nums1, nums2):
        s1, s2 = sum(nums1), sum(nums2)

        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        heapq.heapify(nums1)
        nums2 = [-n for n in nums2]
        heapq.heapify(nums2)
        operations = 0

        diff = s2-s1
        while diff > 0 and nums1 and nums2:
            a = 6-nums1[0]
            b = -1*(nums2[0]+1)

            if a > b:
                heapq.heappop(nums1)
                diff -= a
            else:
                heapq.heappop(nums2)
                diff -= b

            operations += 1

        while diff > 0 and nums1:
            a = 6-nums1[0]
            heapq.heappop(nums1)
            diff -= a
            operations += 1

        while diff > 0 and nums2:
            b = -1*(nums2[0]+1)
            heapq.heappop(nums2)
            diff -= b
            operations += 1

        return operations if diff <= 0 else -1
