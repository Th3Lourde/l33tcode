class Solution:
    def wordBreak(self, s, wordDict):
        dp = [None for _ in range(len(s))]
        words = set()
        maxLength = 0

        for word in wordDict:
            if len(word) > maxLength:
                maxLength = len(word)

            words.add(word)

        def itr(i):
            if i >= len(s):
                return True

            if dp[i] != None:
                return dp[i]

            resp = False

            for wordEnd in range(i+1, min(len(s), i+maxLength)+1):
                subStr = s[i:wordEnd]

                # print(subStr)

                if subStr in words:
                    if itr(wordEnd):
                        resp = True
                        break

            dp[i] = resp
            return dp[i]

        return itr(0)

s = Solution()

print(s.wordBreak("leetcode", ["leet","code"])) # true
print(s.wordBreak("applepenapple", ["apple","pen"])) # true
print(s.wordBreak("applepenapple", ["apple","pen","applepen"])) # true
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # false
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # false
