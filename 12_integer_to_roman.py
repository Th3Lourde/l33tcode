'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
IV            4
IX            9
XL            40
XC            90
CD            400
CM            900

'''

class Solution:
    def intToRoman(self, num):
        value_to_symbol = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i = 0

        romanNum = ""

        while num > 0:
            if values[i] > num:
                i += 1
            else:
                num -= values[i]
                romanNum = romanNum + value_to_symbol[values[i]]

        return romanNum
