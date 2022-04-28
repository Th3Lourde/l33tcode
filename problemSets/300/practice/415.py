class Solution:
    def addStrings(self, num1, num2):
        # 0 Make strs same size
        if len(num1) < len(num2):
            zeroes = "0"*(len(num2)-len(num1))
            num1 = zeroes + num1

        elif len(num1) > len(num2):
            zeroes = "0"*(len(num1)-len(num2))
            num2 = zeroes + num2

        # print(num1)
        # print(num2)

        ans = ""
        carry = 0
        ptr = len(num1)-1

        while ptr >= 0:
            numSum = int(num1[ptr]) + int(num2[ptr]) + carry

            if numSum > 9:
                carry = 1
                numSum -= 10
            else:
                carry = 0

            ans = str(numSum) + ans
            ptr -= 1

        if carry != 0:
            ans = str(carry) + ans

        return ans

print(Solution().addStrings("11", "123"))
print(Solution().addStrings("846", "177"))
print(Solution().addStrings("0", "0"))
