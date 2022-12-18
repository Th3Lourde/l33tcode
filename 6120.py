'''
Given 0-index integer array

In one operation:
- two two ints that are equal
- remove both from nums, forming a pair

Return a 0-indexed int arr of size two
where ans[0] is the number of pairs that are formed
and ans[1] is the number of nms that are left over

create dict
for each value, first ans += 1 for every time you can
divide by two
'''


class Solution:
    def numberOfPairs(self, nums):
        d = {}
        ans = [0,0]

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for key in d:
            ans[0] += d[key]//2
            ans[1] += d[key]%2

        return ans

print(Solution().numberOfPairs([0]))
