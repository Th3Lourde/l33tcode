


class Solution:

    # Optimal solution
    def productExceptSelf(self, nums):
        lp = [1]*len(nums) # False for lp[0]
        for i in range(1, len(nums)):
            lp[i] = lp[i-1]*nums[i-1]

        rp = 1
        for i in range(len(lp)-1, -1, -1):
            lp[i] *= rp
            rp *= nums[i]

        return lp


    # left product, right product solution
    # space complexity is O(2n)
    def productExceptSelf_2(self, nums):
        lp = [1]*len(nums) # False for lp[0]
        for i in range(1, len(nums)):
            lp[i] = lp[i-1]*nums[i-1]

        rp = [1]*len(nums) # False for rp[-1]
        for i in range(len(nums)-2, -1, -1):
            rp[i] = rp[i+1]*nums[i+1]

        ans = [None]*len(nums)
        for i in range(len(nums)):
            ans[i] = lp[i]*rp[i]

        return ans




    def productExceptSelf_1(self, nums):
        prod = 1
        numZ = 0
        zeroI = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]

            elif nums[i] == 0:
                numZ += 1
                zeroI = i


        if numZ > 1:
            return [0]*len(nums)

        elif numZ == 1:
            ans = [0]*len(nums)
            ans[i] = prod
            return ans

        elif numZ == 0:
            ans = [prod]*len(nums)
            for i in range(len(nums)):
                ans[i] -= (nums[i]-1)*ans[i]




if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([4,5,1,8,2,10,6]))
