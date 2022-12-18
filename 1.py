class Solution:
    def twoSum(self, nums, target):
        d = {}

        for idx in range(len(nums)):
            if nums[idx] in d:
                d[nums[idx]].append(idx)
            else:
                d[nums[idx]] = [idx]


        for idx in range(len(nums)):
            t = target-nums[idx]

            if t in d:
                for i in d[t]:
                    if i != idx:
                        return [i, idx]

print(Solution().twoSum([2,7,11,15], 9))
