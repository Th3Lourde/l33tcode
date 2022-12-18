class Solution:
    def findDuplicate(self, nums):
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            count = 0

            # count all elements <= m
            for n in nums:
                if n <= m:
                    count += 1

            if count > m:
                r = m
            else:
                l = m+1

        return l

print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([2,2,2,2,2]))
print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([3,1,3,4,2]))
