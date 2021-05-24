class Solution:
    # Weird DP Solution
    def wiggleMaxLength_1(self, nums):
        if not nums: return 0

        dp = {}

        def itr(idx, targ, comparison):
            if idx >= len(nums):
                return 1

            if (idx, comparison) in dp:
                return dp[(idx, comparison)]

            max_wiggle = 0

            for i in range(idx, len(nums)):
                if comparison == "+":
                    # find first number > targ
                    # actually try out all numbers
                    # as order can matter
                    if nums[i] > targ:
                        max_wiggle = max(max_wiggle, itr(i+1, nums[i], "-") + 1 )

                else:
                    # find first number < targ
                    if nums[i] < targ:
                        max_wiggle = max(max_wiggle, itr(i+1, nums[i], "+") + 1 )

            dp[(idx, comparison)] = max_wiggle
            return dp[(idx, comparison)]

        ans = 1

        # for i in range(len(nums)):
        for i in range(min(2, len(nums))):
            ans = max(ans, itr(i, nums[i], "+"))
            ans = max(ans, itr(i, nums[i], "-"))

        # Either global or scan dp
        # print(dp)
        return ans

    def wiggleMaxLength(self, nums):
        if not nums: return 0
        up, down = 0, 0

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                up = down + 1
            elif nums[i]<nums[i-1]:
                down = up + 1

        return max(up, down)+1

if __name__ == '__main__':
    s = Solution()
    print(s.wiggleMaxLength([1,7,4,9,2,5]))
    print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
