class Solution:
    def twoSum(self, nums, target):
        numToIdx = {}

        for idx, num in enumerate(nums):
            if num in numToIdx:
                numToIdx[num].append(idx)
            else:
                numToIdx[num] = [idx]

        for i, num in enumerate(nums):
            new_target = target-num

            if new_target in numToIdx:
                for idx in numToIdx[new_target]:
                    if idx != i:
                        return [idx, i]


print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([5,5], 10))
