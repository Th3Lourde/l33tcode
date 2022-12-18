'''
Given an integer array nums with possible duplicates,
randomlly output the index of a given target number.

You can assume the given target number exists in the array.

[1, 2, 3, 3, 3]

numToIdxAndOpts = {
    1 : (0, [0])
    2 : (0, [1])
    3 : (0, [2,3,4])
}

'''

class Solution:
    def __init__(self, nums):
        dict = {}
        numToIdxAndOpts = {}

        for idx, num in enumerate(nums):
            if num in dict:
                dict[num].append(idx)
            else:
                dict[num] = [idx]

        for key in dict:
            numToIdxAndOpts[key] = (0, dict[key])

        # print(numToIdxAndOpts)
        self.numToIdxAndOpts = numToIdxAndOpts

    def pick(self, target):
        idx, opts = self.numToIdxAndOpts[target]

        idx += 1

        if idx >= len(opts):
            idx = 0

        self.numToIdxAndOpts[target] = (idx, opts)

        return opts[idx]

s = Solution([1, 2, 3, 3, 3])
print(s.numToIdxAndOpts)

s.pick(3)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
