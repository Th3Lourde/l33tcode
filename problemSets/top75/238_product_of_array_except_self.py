class Solution:
    def productExceptSelf(self, nums):
        prefixProduct = 1

        responseArr = []

        for n in nums:
            responseArr.append(prefixProduct)
            prefixProduct *= n

        suffixProduct = 1

        for i in range(len(nums)-1, -1, -1):
            responseArr[i] *= suffixProduct
            suffixProduct *= nums[i]

        return responseArr

s = Solution()

print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))
