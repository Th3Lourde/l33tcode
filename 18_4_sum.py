
class Solution:
    def fourSum_1(self, nums, target):
        if len(nums) < 4:
            return []

        elif len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            elif sum(nums) != target:
                return []

        ans = []

        for i in range(len(nums)-3):

            for j in range(i+1, len(nums)-2):

                for z in range(j+1, len(nums)-1):

                    for h in range(z+1, len(nums)):

                        if (nums[i] + nums[j] + nums[z] + nums[h]) == target:

                            possible = [nums[i],nums[j],nums[z],nums[h]]
                            possible.sort()

                            if possible not in ans:
                                ans.append(possible)



        return ans

        # Works, is pretty slow
    def fourSum(self, nums, target):
        if len(nums) < 4: return []

        d = {}
        ans = {}

        nums.sort()

        for i in range(len(nums)):
            key = target-nums[i]

            if key in d:
                d[key].append(i)
            else:
                d[key] = [i]

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for z in range(j+1, len(nums)-1):
                    targetKey = nums[i]+nums[j]+nums[z]
                    targetSet = set({i,j,z})

                    if targetKey in d:
                        for idx in d[targetKey]:
                            if idx not in targetSet:
                                possibleAns = [nums[i],nums[j],nums[z],nums[idx]]
                                possibleAns.sort()
                                possibleAns  = tuple(possibleAns)

                                if possibleAns not in ans:
                                    ans[tuple(possibleAns )] = True

        resp = []

        sums =  list(ans.keys())

        for s in sums:
            resp.append(list(s))

        return resp
        # return list(ans.keys())






if __name__ == '__main__':
    s = Solution()

    # nums = [1, 0, -1, 0, -2, 2]
    #
    # target = 0

    nums = [-5,5,4,-3,0,0,4,-2]

    target = 4


    # print(s.fourSum(nums, target))
    # print(s.fourSum([1,0,-1,0,-2,2], 0))
    print(s.fourSum([], 0))
