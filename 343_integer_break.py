import math


class Solution:
    def integerBreak(self, n):

        if n == 2:
            return 1

        t = 0
        i =  1

        while True:
            term_a = 3**(math.floor(math.log(n,3))) - 3**i

            n -= term_a

            print(n)

            term_b = 2**(math.floor(math.log(n,2)))

            if (term_a * term_b) > t:
                t = term_a * term_b

            elif term_a == 0:
                break

            # elif (term_a * term_b) < t:
            #     break



        return t


if __name__ == '__main__':
    s = Solution()

    print(s.integerBreak(10))
