'''
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

"applepenapple"

 wordDict = ["apple","pen"]
'''

class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def traverse(subStr):
            if subStr in wordSet:
                return True

            if subStr in memo:
                return memo[subStr]

            resp = False

            for word in wordSet:
                if word == subStr[:len(word)] and traverse(subStr[len(word):]):
                    resp =  True

            memo[subStr] = resp

            return memo[subStr]

        return traverse(s)

print(Solution().wordBreak("leetcode", ["leet","code"]))
print(Solution().wordBreak("applepenapple", ["apple","pen"]))
print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
