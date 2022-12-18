'''
A message containing A-Z can be encoded into
numbers using the following mapping:
A --> 1
B --> 2
...
Z --> 26

Ok so each number could represent different
characters.

Have an integer --> chr mapping.

when we are out of characters we add to the set

'''

class Solution:
    def numDecodings(self, s):
        intMapping = {
            "1" : "A",
            "2" : "B",
            "3" : "C",
            "4" : "D",
            "5" : "E",
            "6" : "F",
            "7" : "G",
            "8" : "H",
            "9" : "I",
            "10" : "J",
            "11" : "K",
            "12" : "L",
            "13" : "M",
            "14" : "N",
            "15" : "O",
            "16" : "P",
            "17" : "Q",
            "18" : "R",
            "19" : "S",
            "20" : "T",
            "21" : "U",
            "22" : "V",
            "23" : "W",
            "24" : "X",
            "25" : "Y",
            "26" : "Z",
        }

        n = len(s)
        dp = {}

        def itr(idx):
            if idx >= n:
                return 1

            if s[idx:] in dp:
                return dp[s[idx:]]

            resp = 0

            # look one ahead
            if s[idx] in intMapping:
                resp += itr(idx+1)

            # look two ahead
            if idx+1 < n and s[idx:idx+2] in intMapping:
                resp += itr(idx+2)

            dp[s[idx:]] = resp
            return dp[s[idx:]]

        return itr(0)

print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("06"))
