'''
given a string s, find the length of the longest substring
that does not contain repeating characters.

Two pointer problem. Maintain a set that contains the chrs
that are present in the substr. Move right pointer until
we have a dup, every time we add a chr, compare to maxLen.
Then most the left pointer to the right until there are no
duplicates
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        maxLen = float('-inf')
        n = len(s)
        seen = set()

        l = 0
        r = 0

        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                maxLen = max(maxLen, len(seen))
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

        return maxLen
