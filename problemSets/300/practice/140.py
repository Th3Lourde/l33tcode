class Solution:
    def wordBreak(self, s, wordDict):
        ans = []
        prefixSet = set()
        wordSet = set()

        for word in wordDict:
            wordSet.add(word)

            for idx in range(1, len(word)+1):
                prefixSet.add(word[:idx])


        def backtrack(idx, sentence):
            if idx >= len(s):
                ans.append(sentence)
                return

            word = ""

            for i in range(idx, len(s)):
                word += s[i]

                if word not in prefixSet:
                    break

                if word in wordSet:
                    if len(sentence) == 0:
                        backtrack(i + 1, word)
                    else:
                        backtrack(i + 1, sentence+" "+word)

        backtrack(0, "")

        return ans

print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
