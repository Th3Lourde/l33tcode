# https://www.rapidtables.com/convert/number/decimal-to-hex.html
class Solution:
    def toHex(self, num):
        s, res, num = '0123456789abcdef', '', num & 0xFFFFFFFF
        while num:
            res += s[num % 16]
            # Same as dividing by 16
            num >>= 4

        return res[::-1] or '0'
