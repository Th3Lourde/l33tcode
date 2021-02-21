
class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)

        for i in range(len(nums)):
            targ = target-nums[i]
            if targ in d:
                for term in d[targ]:
                    if term != i: return [i, term]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))
    print(s.twoSum([3,3], 6))
