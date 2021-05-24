class Solution:
    def twoSum(self, nums, target):
        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]].append(i)
            else:
                dict[nums[i]] = [i]

        for i in range(len(nums)):
            if target-nums[i] in dict:
                for idx in dict[target-nums[i]]:
                    if idx != i:
                        return [i, idx]

s = Solution()
print(s.twoSum([2,7,11,15], 9))
