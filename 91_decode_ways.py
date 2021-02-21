'''
TCs:
"12"
"226"
"0"
"425"
"420"
"426"
"190"
"191"
"121"
"150"
"9"
"10"
"29"
"1"
"11"
"111"
"1111"
"11111"

"1201234"
"120120324"
"120120328"

"110"

'''

class Solution:
    def numDecodings(self, s):
        decode = set({'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'})
        n = len(s)

        if n == 1:
            if s in decode: return 1
            return 0

        if s[0] == "0":
            return 0

        # One pass to remove trailing zeroes and
        # check for undecodable strs
        for i in range(len(s)-1):
            if s[i:i+2] == "00":
                return 0

            if s[i+1] == "0" and s[i:i+2] not in decode:
                return 0


        dp = [0 for _ in range(len(s))]
        dp[0] = 1

        if s[1] in decode:
            dp[1] += 1

        if s[:2] in decode:
            dp[1] += 1

        for i in range(2, len(s)):
            s1=0
            s2=0
            s3=0

            if s[i] == "0":
                if s[i-1:i+1] in decode:
                    dp[i] = dp[i-2]
                continue

            if s[i-1:i] in decode:
                s1 = dp[i-1]

            if s[i-1:i+1] in decode:
                s2 = dp[i-2]

            if s[i-1] == "0":
                s3 = dp[i-1]

            dp[i] = s1+s2+s3

        if s[-2] == "0":
            return dp[-2]

        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("110"))
