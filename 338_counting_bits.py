
'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Input: 2
Output: [0,1,1]

Input: 5
Output: [0,1,1,2,1,2]

the length of the output array is = |num|+1
I guess we count zero

bin(0):  0
bin(1):  1
bin(2):  10
bin(3):  11
bin(4):  100
bin(5):  101
bin(6):  110
bin(7):  111
bin(8):  1000
bin(9):  1001
bin(10): 1010
bin(11): 1011

I feel like we are supposed to be doing this with dynamic programming

















assuming number is greater 0
ans = [0] * (num+1)
exp = "0"
i = 1
count = 0
while i < num:
    #update
    # case 1: there is a zero in the expression

    if "0" in exp:
        j = len(exp)-1
        # find zero, in expression, set



    i += 1




So how to quickly calculate the number of 1's in the binary expression of a number:
import math

if n == 0:
    0
elif n == 1:
    1
elif int(math.log2(n)) == math.log2(n):
    # meaning that if casting the output as an int is numerically equal to that number

if n = 2^x x \in Z: 1


if there is not a zero in the expression:
exp = "11"
if 0 not in exp:
    exp = "1"+len(exp)*"0"
'''

'''
[itr] (1)
[1]
ones = 1

[itr] (2)
ones = len(repr)
[1, 0] // add a zero
ones = 1 // set ones to 1

[itr] (3)
[1, 1]
ones = 2

[itr] (4)
ones = len(repr)
[1, 0, 0] // add a zero
ones = 1 // set ones to 1

[itr] (5)
[1, 0, 1]
ones = 2

[itr] (6)
[1, 1, 0] // write one, set all ones on rhs to zero.
ones = 3

-------------------------------------------------------------

[itr] (1)
[1]
ones = 1

- if number of ones == len() → put one one on lhs, all others to zeros, append zero
- start from rhs, find a zero (counting the number of ones we see when going r → l)
|--> when we have found a zero, set it to one. Set all ones on rhs to zero.


'''


class Solution:
        # 'Slow' version
    def countBitsS(self, num):
        if num == 0:
            return [0]

        ans = [0] * (num+1)

        i = 1

        while i <= len(ans)-1:
            # count = number of ones in binary expression of i
            tmp = bin(i)
            tmp = tmp[2:]
            count = 0

            for j in range(len(tmp)):
                if tmp[j] == "1":
                    count += 1

            ans[i] = count

            i += 1

        return ans

        # Not sure if I have the time complexity correct here
        # Thought it was o(n), however the number of adjustments we are making
        # when adding in binary is based upon size of number, idk
    def countBits_1(self, num):
        # simulate addition in binary
        repr = [0]
        ones = 0
        ans = [0]

        for i in range(num):
            if ones == len(repr):
                repr = [1] + [0 for i in range(len(repr))]
                ones = 1
            else:
                p = len(repr)-1
                sub = 0

                # find a zero
                while repr[p] != 0:
                    p -= 1
                    sub += 1

                # replace it with one
                repr[p] = 1
                ones += 1

                if p != len(repr)-1:
                    repr = repr[:p+1] + [0 for i in range(sub)]
                    ones -= sub

            ans.append(ones)

        return ans

    def countBits(self, num):
        ans = [0]

        for i in range(1, num+1):
            if i % 2 == 0:
                ans = ans[i>>1]
            else:
                ans = ans[i-1] + 1



if __name__ == '__main__':
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))
