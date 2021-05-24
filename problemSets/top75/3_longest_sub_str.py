'''
Given a string s, find the length of the longest substring without repeating characters.

Create all substrings that don't have repeating characters.

This would be 0(n²).

seen = {
    "a": 3
    "b": 4
    "c": 2

}

 01234567
"abcabcbb"
   l
     r

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}

        maxLength = 0

        l = 0
        r = 0

        while r < len(s):
            while s[r] in seen:
                del seen[s[l]]
                l += 1


            seen[s[r]] = r
            r += 1

            maxLength = max(maxLength, len(seen))

        return maxLength

print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring("")) # 0
