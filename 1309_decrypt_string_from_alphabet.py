'''
Given string s.

0-9 represent 'a' to 'i'
10#-#26 represent 'j' to 'z'


Return the string after mapping.

The question is how do we know we looking at a
single digit or double?

What if we go through the list backwards? The #-sign
occurs at the end. If we see a '#', we know to look left two.

What would be nice is if we already know the unicode char.

ord("a") = 97

So take char of num + 96

if not #, go left one, cast as int, add 96, append the chr
if #, go left one, two, case as int, ...

append on the lhs of the string

12#
'''

class Solution:
    def freqAlphabets(self, s):
        i = len(s)-1

        ans = ""

        while i >= 0:
            if s[i] == "#":
                ans = chr(int(s[i-2: i])+96) + ans
                i -= 3

            elif s[i] != "#":
                ans = chr(int(s[i])+96) + ans
                i -= 1

        return ans


if __name__ == '__main__':
    s = Solution()

    # print(s.freqAlphabets("10#11#12"))
    # print(s.freqAlphabets("1326#"))
    # print(s.freqAlphabets("25#"))
    # print(s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
    # print(s.freqAlphabets(""))
