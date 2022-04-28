
'''
Ok so calculate the right product
then calculate the left product

[0,1,2,3]
RHS
1*2*3,2*3,*3,1
LHS
1,0*,0*1,0*1*2

'''

class Solution:
    def productExceptSelf(self, nums):
        resp = [1 for _ in range(len(nums))]

        lProd = 1
        for i in range(1, len(nums)):
            lProd *= nums[i-1]
            resp[i] *= lProd

        rProd = 1
        for i in range(len(nums)-2, -1, -1):
            rProd *= nums[i+1]
            resp[i] *= rProd

        return resp

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1,1,0,-3,3]))
