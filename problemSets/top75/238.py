'''
nums[i] = nums[0:i-1]*nums[i+1:]

[1,2,3,4]

leftProduct = [i, i*i+1, i*i+1*i+2, i*i+1*i+2*i+3]
rightProduct = []
'''



class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        l = [0]*n
        r = [0]*n
        ans = []

        for i in range(len(nums)):
            if i == 0:
                l[i] = nums[i]
            else:
                l[i] = l[i-1]*nums[i]

        for i in range(len(nums)-1, -1, -1):
            if i == n-1:
                r[i] = nums[i]
            else:
                r[i] = r[i+1]*nums[i]

        for i in range(n):
            lIdx = i-1
            rIdx = i+1

            if lIdx > -1 and rIdx < n:
                ans.append(l[lIdx]*r[rIdx])

            elif lIdx > -1:
                ans.append(l[lIdx])

            elif rIdx < n:
                ans.append(r[rIdx])

            else:
                ans.append(0)

        return ans


print(Solution().productExceptSelf([1,0]))
