'''
1) Sort the array and check for duplicates
2) Maintain a dict and perform stores/look-ups
'''

class Solution:
    def containsDuplicate(self, nums):
        d = {}

        for n in nums:
            if n in d:
                return True
            d[n] = True

        return False

print(Solution().containsDuplicate([1,2,3]))
