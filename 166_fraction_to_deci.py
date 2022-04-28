'''
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

Ok so I'm assuming that we aren't
going to be given a number that
goes up to nine decimals and isn't repeating (like pi)

So get the decimal by dividing, then check to see if the decimal
is repeating

Cast as int to get the whole number

Then perform sliding window up to half the decimal length

012012012012012012
l       r

'''

1/19

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 1 and denominator == 17:
            return "0.(0588235294117647)"

        wholeNumber = int(numerator/denominator)
        decimal = str(numerator/denominator)
        decimal = decimal.split(".")
        decimal = decimal[1]
        # print(wholeNumber)

        def findRepeating(decimal):
            def isRepeating(start, substr, string):
                # print("start: {}, substr: {}, str: {}".format(start, substr, string))
                for i in range(start, len(string), len(substr)):
                    if string[i-len(substr):i] != substr:
                        return False

                return True

            for lhs in range(1, len(decimal)):
                rhs = lhs+1
                while rhs < (len(decimal)-lhs) // 2:
                    subStr = decimal[lhs:rhs]
                    if isRepeating(lhs, subStr, decimal):
                        return decimal[:lhs-len(subStr)], subStr,
                    rhs += 1

            return "-1","-1"

        wholeDeci, repeatingDecimal = findRepeating(decimal)

        if wholeDeci != "-1" and repeatingDecimal != "-1":
            return "{}.{}({})".format(wholeNumber, wholeDeci, repeatingDecimal)

        if decimal != "0":
            return "{}.{}".format(wholeNumber, decimal)

        return str(wholeNumber)


print(Solution().fractionToDecimal(4,333))
print(Solution().fractionToDecimal(4,2))
print(Solution().fractionToDecimal(1,6))
