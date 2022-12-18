'''
Given a string s, return t/f depending on
if s can be composed of the elements of wordDict,
you can use the same words from wordDict multiple times

applepenapple
l
      r

{
a
ap
app
appl
apple
p
e
n
}
'''

class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set()
        prefixSet = set()
        n = len(s)
        cache = {}

        for word in wordDict:
            wordSet.add(word)

            for idx in range(len(word)):
                prefixSet.add(word[:idx+1])

        def itr(idx):
            if idx >= n:
                return True

            if idx in cache:
                return cache[idx]

            resp = False

            for i in range(idx+1, n+1):
                prefix = s[idx:i]

                if prefix in wordSet and itr(i):
                    resp = True
                    break

                if prefix not in prefixSet:
                    break

            cache[idx] = resp
            return cache[idx]


        return itr(0)

print(Solution().wordBreak("applepenapple", ["apple","pen"]))
