# class Solution:
#     def longestPalindrome(self, word1, word2):
#         ans = 0
#         s = set()
#         for l in range(0, len(word2)):
#             for r in range(l+1, len(word2)):
#                 w = word2[l:r+1]
#                 s.add(w[::-1])
#
#         for l in range(0, len(word1)):
#             for r in range(l+1, len(word1)):
#                 w = word1[l:r+1]
#
#                 if len(w)%2 == 0:
#                     t = w[:len(w)-1]
#
#                     if t in s:
#                         ans = max(ans, len(t)+len(t)+1)
#
#                 else:
#
