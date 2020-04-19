

class Solution:

    def convert(self, s, numRows): # Does not work, need alternate formula for space between terms. Come back to later?

        if numRows <= 1 or len(s) == 0 or numRows >= len(s):
            return s

        ans = ""

        for x in range(numRows):
            term = x
            while term < len(s):
                ans += s[term]
                term += (numRows-1)*2

        return ans


    def convert1(self, s, numRows): # This works

        if numRows <= 1 or len(s) == 0 or numRows >= len(s):
            return s

        zig = 0
        # slope = 1
        i = 0
        ans = ["" for i in range(numRows)]

        while i <= len(s)-1:
            ans[zig] += s[i]

            if zig == 0:
                slope = 1

            if zig == numRows-1:
                slope = -1

            zig += slope

            i += 1

        return "".join(ans)
