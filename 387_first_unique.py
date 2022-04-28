'''
Given a string s, find the first non-repeating character
in it and return its index. If it does not exist, return -1.

What if we have a chr --> idx dict

1 pass to find the first chr that doesn't repeat
'''


class Solution:
    def firstUniqChar(self, s):
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = set({i})
            else:
                d[s[i]].add(i)

        ans = float('inf')

        for k in d.keys():
            if len(d[k]) == 1:
                ans = min(ans, d[k].pop())

        if ans == float('inf'):
            return -1

        return ans

print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
print(Solution().firstUniqChar(""))
print(Solution().firstUniqChar("a"))
print(Solution().firstUniqChar("ab"))
print(Solution().firstUniqChar("aba"))
print(Solution().firstUniqChar("aab"))
