'''
So given a romand numeral, convert it to an int.

So there are some special cases that we should consider.

Can just write some edge cases to cover this
'''

class Solution:
    def romanToInt(self, s):
        chrToNum = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        }

        ans = 0
        idx = 0

        while idx < len(s):
            if idx != len(s)-1:
                if s[idx:idx+2] == "IV":
                    ans += 4
                    idx += 2
                elif s[idx:idx+2] == "IX":
                    ans += 9
                    idx += 2
                elif s[idx:idx+2] == "XL":
                    ans += 40
                    idx += 2
                elif s[idx:idx+2] == "XC":
                    ans += 90
                    idx += 2
                elif s[idx:idx+2] == "CD":
                    ans += 400
                    idx += 2
                elif s[idx:idx+2] == "CM":
                    ans += 900
                    idx += 2
                else:
                    ans += chrToNum[s[idx]]
                    idx += 1
            else:
                ans += chrToNum[s[idx]]
                idx += 1

        return ans
