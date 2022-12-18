class Solution:
    def findMissingRanges(self, nums, lower, upper):
        resp = []

        if len(nums) == 0:
            if lower == upper:
                return ["{}".format(lower)]
            else:
                return ["{}->{}".format(lower, upper)]

        elif len(nums) == 1:
            # check lower bound
            if nums[0] != lower:
                resp.append("{}->{}".format(lower, nums[0]-1))

            # check upper bound
            if nums[0] != upper:
                resp.append("{}->{}".format(nums[0]+1, upper))

        else:
            # check lower bound
            if nums[0] != lower:
                resp.append("{}->{}".format(lower, nums[0]-1))

            for i in range(len(nums)-1):
                if nums[i]+1 != nums[i+1]:
                    resp.append("{}->{}".format(nums[i]+1, nums[i+1]-1))

            if nums[-1] != upper:
                resp.append("{}->{}".format(nums[-1]+1, upper))


        for idx, missingRange in enumerate(resp):
            rangeList = missingRange.split("->")

            if rangeList[0] == rangeList[1]:
                resp[idx] = rangeList[0]

        return resp

print(Solution().findMissingRanges([1,2], 0, 9))
print(Solution().findMissingRanges([], 1, 1))
print(Solution().findMissingRanges([2], 0, 4))
print(Solution().findMissingRanges([0,1,3,50,75], 0, 75))
