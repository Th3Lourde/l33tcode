
'''
An integer has sequential digits
iff each digit in the number
is one more than the previous digit.

Return a sorted list of all the integers
in the range [lo, hi] that have sequential
digits.

Start with the smallest numbers first (ofc)

Have a function with a starting value and a
target length.

Use the length, as well as the value of the
hi to determine what gets called.

if len(low) == len(hi), then we can also
include a max val argument

f(lo, hi, len) | generate all sequential numbers of len len starting at lo and ending b4 hi.


for low in range(lo, hi):
    num = []

    while low < hi and len(num) < len:
        num.append("{}".format(low))
        low += 1

    if len(num) == len:
        # Have valid ans
        tmp = "".join(num)
        ans.append(int(tmp))



--------------------------------------------------

100, 300

f(1, 3, 3)

So once we get one solution we keep going through the next
ones.

We also have a largest value that we can never go larger than.

Also have a list of options?

What would the initial pass be?

opts = [i for i in range(10)]
initialOpts = [i for i in range(low, 10)]

firstRound = []
targetLen = # size of low

upperBound = 10

if len(high) == len(low):
    upperBound = firstDigitOfUpper


for i in range(firstDigitOfLow, upperBound):
    term = str(i)
    j = i+1
    while len(term) < len(low) and j in opts:
        term += str(j)
        j += 1

    if low <= int(term) <= high:
        # Is valid, continue

(lower, upper, opts)

def itr()

What if we did something else,

600

678
789

Add both to answer

call func --> (4)

1234
2345
3456
4567
5678
6789


def itr(targetLen):


We could handle two cases:
   - Where target len == low, high, or both
   - or Neither

What if we just set high and low based upon those conditions

We call the function with += 1 for targetLen ⟺ ≠ len(high)


'''

class Solution1:
    def sequentialDigits(self, low, high):
        ans = []

        lowI = low
        highI = high

        low = str(low)
        high = str(high)
        firstDL = int(low[0])

        def itr(lo, hi, l):

            for low in range(lo, hi+1):
                num = []

                while low <= 9 and len(num) < l:
                    num.append("{}".format(low))
                    low += 1

                if len(num) == l:
                    # Have valid ans
                    tmp = "".join(num)
                    tmp = int(tmp)

                    if lowI <= tmp <= highI:
                        ans.append(int(tmp))

        c = len(low)

        while c <= len(high):

            if c == len(low):
                itr(firstDL, 9, c)
                c += 1

            elif c == len(high):
                itr(1, int(high[0]), c)
                c += 1

            else:
                itr(1, 9, c)

        return ans

        # e.g. 10, 2000, set({1-9}) <-- These should be given as strings
        # upper, lower within scope of function

class Solution:

    def sequentialDigits(self, low, high):

        lenLow = len(str(low))
        lenHigh = len(str(high))

        ldLow = int(str(low)[0])
        ldHigh = int(str(high)[0])

        def itr(targetLen):
            lowD = ldLow if targetLen == lenLow else 1
            highD = ldHigh if targetLen == lenHigh else 9

            # [1,2,3,4,5,6,7,8] l = 3
            for i in range(lowD, highD+1):
                term = str(i)
                j = i + 1

                while len(term) < targetLen and int(j) < 10:
                    term += str(j)
                    j = j+1

                if low <= int(term) <= high and len(term) == targetLen:
                    ans.append(int(term))

            if targetLen != lenHigh:
                itr(targetLen+1)

        ans = []

        itr(lenLow)

        return ans







    def sequentialDigits_1(self, low, high):
        def itr(term, targetLen):

            if term == "":
                # Build
                lwr = int(str(low)[0])
                upr = 9

                if len(str(low)) == len(str(high)):
                    upr = int(str(high)[0])

                for i in range(lwr, upr):
                    term = str(i)
                    j = i+1

                    while len(term) < len(str(low)) and j < 10:
                        term += str(j)
                        j += 1

                    if low <= int(term) <= high:
                        ans.append(int(term))
                        itr(str(term), len(str(low))+1)



            else:
                # Go for target length + 1
                while low <= int(term+str(int(str(term)[-1])+1)) <= high and int(str(term)[-1])+1 < 10:
                    term += str(int(str(term)[-1])+1)
                    ans.append(int(term))

        ans = []

        minV = int(str(low)[0])

        itr("", len(str(low)), )

        ans.sort()

        # print(ans)
        return ans

# I don't think that we need opts



if __name__ == '__main__':
    s = Solution()

    print(s.sequentialDigits(100, 300))


    print(s.sequentialDigits(10, 10000))
    # print(s.sequentialDigits(1000, 13000))

    assert s.sequentialDigits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]

    assert s.sequentialDigits(100, 3000) == [123, 234, 345, 456, 567, 678, 789, 1234, 2345]

    assert s.sequentialDigits(100, 300) == [123, 234]

    assert s.sequentialDigits(200, 300) == [234]

    assert s.sequentialDigits(200, 900) == [234, 345, 456, 567, 678, 789]

    assert s.sequentialDigits(100, 900) == [123, 234, 345, 456, 567, 678, 789]

    assert s.sequentialDigits(1000, 10000) == [1234, 2345, 3456, 4567, 5678, 6789]

    # 10
    # 1000000000
