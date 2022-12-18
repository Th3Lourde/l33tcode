'''
Write a function to find the longest common prefix string amongst an array of strings.

So many pointer?

'''

class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        ptr = 0

        if "" in strs or len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        def allEqual(ptr):
            for idx in range(len(strs)-1):
                if ptr >= len(strs[idx]) or ptr >= len(strs[idx+1]):
                    return False

                if strs[idx][ptr] != strs[idx+1][ptr]:
                    return False
            return True

        while allEqual(ptr):
            prefix = strs[0][0:ptr+1]
            ptr += 1

        return prefix
