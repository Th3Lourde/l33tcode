'''
Ok so mis-read question, word.

So we can change the order of the elements

Not sure about 0(n) time, but we can def do it in nlogn time
'''

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        exists = set()
        cache = {}
        ans = 1

        for n in nums:
            exists.add(n)

        def itr(n):
            if n not in exists:
                return 0

            if n in cache:
                return cache[n]

            ans = 1 + itr(n+1)
            cache[n] = ans
            return cache[n]

        for n in nums:
            # so if n serves as the beginning of a consecutive sequence,
            # how long will that sequence be?

            ans = max(ans, itr(n))

        return ans








print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,3,7,2,5,8,4,6,0,1]))
