'''
Write a function to find the longest common prefix string amongst
an array of strings

pick the longest prefix as the first string
then compare to each other word, return the chrs that
they have in common
'''

class Solution:
    def longestCommonPrefix(self, strs):

        def findCommonPrefix(word1, word2):
            idx = 0
            while idx < min(len(word1), len(word2)):
                if word1[idx] == word2[idx]:
                    idx += 1
                else:
                    break

            return word1[:idx]

        if len(strs) == 0:
            return ""

        elif len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for idx in range(1, len(strs)):
            prefix = findCommonPrefix(prefix, strs[idx])

            if prefix == "":
                return prefix

        return prefix

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
