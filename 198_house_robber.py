'''
Given a list of non-negative integers (value of each house)
determine the maximum amount of money you can retrieve.

You can't hit adjacent houses

'''

class Solution:
    def rob_1(self, nums):
        '''
        Ok so you can't rob adjacent houses.
        My initial thought is that you just sum
        the values of the evenly numbered houses
        and compare that to the sum of the oddly
        numbered houses, and return the max value
        '''
        odd = 0
        even = 0

        bool = True

        for i in range(len(nums)):
            if bool:
                even += nums[i]
                bool = False
            elif not bool:
                odd += nums[i]
                bool = True

        return max(odd, even)

    def robDP(self, nums):
        # EDGE CASES

        if len(nums) == 0:
            return 0

        elif len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return max(nums[0], nums[1])

        elif len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])

        dp = [0 for _ in range(len(nums))]

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + dp[0]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])

        return max(dp[-1], dp[-2])

    def rob(self, nums):
        if len(nums) == 0:
            return 0

        elif len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return max(nums[0], nums[1])

        elif len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])

        nums[2] += nums[0]

        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])

        return max(nums[-1], nums[-2])



if __name__ == '__main__':
    s = Solution()

    houses = [1,2,3,1]
    houses = [2,7,9,3,1]


    print(s.rob(houses))
