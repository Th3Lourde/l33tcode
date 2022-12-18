class Solution:
    def maximumsSplicedArray(self, nums1, nums2):
        ans = max(sum(nums1), sum(nums2))
        diff1 = [nums2[i] - nums1[i] for i in range(len(nums1))]
        diff2 = [nums1[i] - nums2[i] for i in range(len(nums1))]

        def kadane(diffArr):
            if len(diffArr) == 0:
                return 0

            maxSum = max(diffArr)
            currSum = 0

            for num in diffArr:
                currSum += num

                if currSum < 0:
                    currSum = 0
                elif (currSum > maxSum):
                    maxSum = currSum

            return maxSum

        return max(sum(nums1)+kadane(diff1), sum(nums2)+kadane(diff2))




print(Solution().maximumsSplicedArray([1,1,1,1,50],[1,10,1,10,1]))

print(Solution().maximumsSplicedArray([60,60,60],[10,10,90] ))
