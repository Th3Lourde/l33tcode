# https://leetcode.com/problems/add-bold-tag-in-string/discuss/104269/Python-Straightforward-with-Explanation
class Solution:
    def addBoldTag(self, s, words):
        validSubStr = set()
        validWord = set()
        marked = set()

        for word in words:
            for i in range(1,len(word)):
                subWord = word[:i]
                validSubStr.add(subWord)
            validWord.add(word)

        # print("b" in validWord)

        for l in range(0,len(s)):
            for r in range(l, len(s)+1):
                if s[l:r+1] in validSubStr:
                    continue
                elif s[l:r+1] in validWord:
                    for idx in range(l, r+1):
                        marked.add(idx)
                else:
                    break

            if s[l] in validWord:
                marked.add(l)


        wrapped = False
        ans = ""

        for idx in range(len(s)):
            if idx in marked:
                if wrapped == False:
                    wrapped = True
                    ans += "<b>"
                    ans += s[idx]
                else:
                    ans += s[idx]
            else:
                if wrapped:
                    ans += "</b>"
                    wrapped = False

                ans += s[idx]

        if len(s)-1 in marked:
            ans += "</b>"


        return ans

print(Solution().addBoldTag("58695abcdxyz123", ["58695", "695a", "abcd","cdxyz", "6"]))
print(Solution().addBoldTag("abcxyz123", ["abc","123"]))
print(Solution().addBoldTag("aaabbcc", ["a","b","c"]))
print(Solution().addBoldTag("aaabbcc", ["aaa","aab","bc"]))
