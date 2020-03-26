'''
Given n
return a string with n characters
Each character occurs an odd number of times

if n is even, add xy n/2 times
if n is odd, add xy (n-1)/2 times, + z



'''


class Solution:
    def generateTheString(self, n):

        if n == 0:
            return ""

        if n % 2 == 0:
            return "x"*(n-1)+"y"

        elif n % 2 != 0:
            return "x"*(n)
