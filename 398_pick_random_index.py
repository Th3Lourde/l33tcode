class Solution:
    def __init__(self, nums):
        elements = {}

        for i in range(len(nums)):
            if nums[i] not in elements:
                elements[nums[i]] = [[i], 0]
            else:
                elements[nums[i]][0].append(i)

        self.elements = elements


    def pick(self, target):
        if target not in self.elements:
            return None

        idx = self.elements[target][1]
        idx += 1

        if idx >= len(self.elements[target][0]):
            idx = 0

        self.elements[target][1] = idx

        return self.elements[target][0][self.elements[target][1]]

s = Solution([1, 2, 3, 3, 3])

print(s.pick(3))
