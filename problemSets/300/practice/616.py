'''
Given string s and an array of strings words


So create trie out of words.

two pointer on s.

every time we hit a substr that dne in set,
move left one, reset the string to the right most chr
continue from there

"aaabbcc", ["aaa","aab","bc"]

substrs = {
a
b
aa
bc
aaa
aab
}
1233110
aaabbcc
    l
     r
'''

class Solution:
    def addBoldTag(self, s, words):
        substrs = set()
        ans = ""

        for word in words:
            for idx in range(len(word)+1):
                if idx != 0:
                    substrs.add(word[0:idx])


        isIdxSubStr = {}

        for i in range(0, len(s)):
            isIdxSubStr[i] = False

        for l in range(0, len(s)):
            for r in range(l+1, len(s)+1):
                if s[l:r] in substrs:
                    isIdxSubStr[r-1] = True

        print(isIdxSubStr)

        l = 0
        subStr = ""

        while l < len(s):
            shouldWrap = False
            subStr = s[l]

            if isIdxSubStr[l]:
                shouldWrap = True

                r = l+1

                while r < len(s) and isIdxSubStr[r]:
                    subStr += s[r]
                    r += 1

                l = r-1

            if shouldWrap:
                subStr = "{}{}{}".format("<b>", subStr, "</b>")

            ans += subStr
            l += 1

        return ans

'''
subStr = a

aabbcc
l
r
'''


print(Solution().addBoldTag("aabbcc", ["a", "b", "c"]))
# No wrap

# No wrap
print(Solution().addBoldTag("aabbc", []))
# wrap left to mid
print(Solution().addBoldTag("aabbc", ["aab"]))
# wrap mid to right
print(Solution().addBoldTag("aabbc", ["bbc"]))
# 2 adj wrap left
print(Solution().addBoldTag("aabbc", ["aab","bb"]))
# 2 adj wrap right
print(Solution().addBoldTag("zabbc", ["ab","bb"]))
# 3 adj wrap
print(Solution().addBoldTag("zabbc", ["z","ab","bb"]))
# 1 overlapping wrap
print(Solution().addBoldTag("zaabbc", ["zab","aabb"]))

print(Solution().addBoldTag("aabbc", ["aaa","aab","bc"]))

print(Solution().addBoldTag("aaabbcc", ["aaa","aab","bc"]))

print(Solution().addBoldTag("abcxyz123", ["abc","123"]))
# Check full string
