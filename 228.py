class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        ranges = []

        lo = nums[0]
        hi = ""

        for idx in range(1, len(nums)):
            if nums[idx-1]+1 != nums[idx]:
                hi = nums[idx-1]

                if lo == hi:
                    ranges.append("{}".format(lo))
                else:
                    ranges.append("{}->{}".format(lo,hi))

                lo = nums[idx]
                hi = ""

            if idx == len(nums)-1:
                hi = nums[idx]

                if lo == hi:
                    ranges.append("{}".format(lo))
                else:
                    ranges.append("{}->{}".format(lo,hi))


        return ranges

print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
print(Solution().summaryRanges([]))
print(Solution().summaryRanges([-1]))
print(Solution().summaryRanges([1]))
