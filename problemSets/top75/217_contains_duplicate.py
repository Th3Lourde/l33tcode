class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False

s = Solution()

print(s.containsDuplicate([1,2,3]))
