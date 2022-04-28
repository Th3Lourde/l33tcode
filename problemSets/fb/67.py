'''
Given two binary strings a and b, return their sum as a binary string.

a = "1010"
b = "1011"

1010
1011
   ^

carry = 0
sum =  ""

localSum = int("0") + int("1") + carry

if localSum  == 0:
    carry = 0
    sum = "0" + sum
elif localSum == 1:
    carry = 1
    sum = "0" + sum
elif localSum == 2:
    carry = 1
    sum = "1" + sum

if carry == 1:
    sum = "1" + sum


'''

class Solution:
    def addBinary(self, a, b):
        carry = 0
        sum = ""

        # 1) Make the strings the same size
        while len(a) < len(b):
            a = "0" + a

        while len(b) < len(a):
            b = "0" + b

        i = len(b)-1

        # Add the strings
        while i >= 0:
            localSum = int(a[i]) + int(b[i]) + carry

            if localSum == 0:
                carry = 0
                sum = "0" + sum

            elif localSum == 1:
                carry = 0
                sum = "1" + sum

            elif localSum == 2:
                carry = 1
                sum = "0" + sum

            elif localSum == 3:
                carry = 1
                sum = "1" + sum

            i -= 1

        # If there's something left, add here
        if carry == 1:
            sum = "1" + sum

        return sum


print(Solution().addBinary("1111", "1"))
print(Solution().addBinary("1000100", "00100"))
