

class Solution:
    def fourSum(self, nums, target):
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



if __name__ == '__main__':
    s = Solution()

    # nums = [1, 0, -1, 0, -2, 2]
    #
    # target = 0

    nums = [-5,5,4,-3,0,0,4,-2]

    target = 4


    print(s.fourSum(nums, target))
