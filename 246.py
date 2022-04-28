'''
Given a string which represents an integer,
return true if num is a strobogrammic number.

a strobogrammic number is a number that looks the
same when rotate 180 degrees

So let's record the list of numbers that, when flipped,
have a counter part.

Then have a two pointer, one from start, another from end,
see if those numbers, when flipped are each other's counter part.

0 --> 0
6 --> 9
8 --> 8
9 --> 6

'''

class Solution:
    def isStrobogrammatic(self, num):
        chrToFlipped = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6",
        }

        l = 0
        r = len(num)-1

        while l <= r:
            if num[l] not in chrToFlipped or num[r] not in chrToFlipped:
                return False
            elif chrToFlipped[num[l]] != num[r]:
                return False

            l += 1
            r -= 1

        return True

print(Solution().isStrobogrammatic("69"))
print(Solution().isStrobogrammatic("010"))
print(Solution().isStrobogrammatic("619"))
