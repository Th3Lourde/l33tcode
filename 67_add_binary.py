class Solution:
    def addBinary(self, a, b):
        ans = ""
        carry = 0

        aPointer = len(a)-1
        bPointer = len(b)-1

        while aPointer >= 0 or bPointer >= 0:
            aVal = 0

            if aPointer >= 0:
                if a[aPointer] == '1':
                    aVal = 1
                aPointer -= 1

            bVal = 0

            if bPointer >= 0:
                if b[bPointer] == '1':
                    bVal = 1
                bPointer -= 1

            summation = aVal + bVal + carry

            if summation == 0:
                carry = 0
                ans = "0" + ans
            elif summation == 1:
                carry = 0
                ans = "1" + ans
            elif summation == 2:
                carry = 1
                ans = "0" + ans
            else:
                # summation == 3
                carry = 1
                ans = "1" + ans

        if carry == 1:
            ans = "1" + ans

        return ans

s = Solution()
print(s.addBinary("1010", "1011"))
print(s.addBinary("11", "1"))
print(s.addBinary("111111", "101010101"))
