

class Solution:
    '''
    Given a positive integer n, find the least number of perfect
    square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

    So we have numbers that are perfect squares,
    our goal is to select the least number of
    perfect squares that result in our answer

    So start at the largest perfect square that is less than
    our input, subtract from input.

    Continue until we get to 1
    1^2 = 1
    2^2 = 4
    3^2 = 9
    4^2 = 16
    5^2 = 25
    ...

    The first question that I am running into is: What number do we start with first?
    Or: How do we find the largest perfect square that is less than or equal to our input?

    * We can take the square root of the number
    * If the number is of type float:
        - Find the floor of that number: that is what we start with
    * If the number is of type int:
        - Then the number given is a perfect square, return 1

    Ok so this approach doesn't work for all inputs. It doesn't work for 12.

    9 + 1 + 1 + 1 <-- has more numbers in it than --> 4 + 4 + 4

    Ok, so how do we then recognize when this case is going to occur?
    Problem for tomorrow :)
    '''

    def numSquares(self, n):
        import math

        ans = 0

        sqrt = math.sqrt(n)

        if type(sqrt) == float:
            ans += 1
            n -= int(math.floor(sqrt))**2

        elif type(sqrt) == int:
            return 1

        while n > 3:
            sqrt = math.sqrt(n)

            if type(sqrt) == float:
                ans += 1
                n -= int(math.floor(sqrt))**2

            elif type(sqrt) == int:
                ans += 1
                print("This shouldn't have happened...")
                return ans

        return ans + n


    def get_guess(self, a, b):
        return (4**a)*(8*b + 7)

    def numSquares_math(self, n):
        # this is the math solution found on l33tcode
        import math

        if n == 0:
            return 0

        # Case: 1
        # if the sqrt(n) is an integer,
        # the input is a perfect square
        if math.sqrt(n) == int(math.sqrt(n)):
            return 1

        # Case: 4
        a = 0
        b = 0

        while True:
            if b == 0 and self.get_guess(a,b) > n:
                # can't be four, move on
                break

            while self.get_guess(a,b) < n:
                b += 1

            if self.get_guess(a,b) == n:
                return 4

            # iterate a, reset b
            a += 1
            b = 0


        # Case: 2
        i = 1
        while i**2 < n:
            tmp = math.sqrt(int(n-(i**2)))

            if (tmp) == int(tmp):
                return 2
            i += 1

        return 3

    def numSquares_dp(self, n):
        import math
        if n <= 0:
            return 0

        elif math.sqrt(n) == int(math.sqrt(n)):
            return 1

        elif n == 2:
            return 2

        elif n == 3:
            return 3

        # generate perfect square integers < n
        ps = []
        tmp = []
        tmp2 = set()

        for i in range(1, n):
            if i**2 < n:
                ps.append(i**2)
                tmp.append(n - i**2)
                tmp2.add(n - i**2)

            elif i**2 > n:
                break

        # print("n: {}".format(n))
        # print("ps: {}".format(ps))
        # print("tmp: {}".format(tmp))

        use_set = True
        ans = 2
        stop = len(tmp)

    #
    # def numSquares(self, n):
    #     if n < 2:
    #         return n
    #     lst = []
    #     i = 1
    #     while i * i <= n:
    #         lst.append( i * i )
    #         i += 1
    #     cnt = 0
    #     toCheck = {n}
    #     while toCheck:
    #         cnt += 1
    #         temp = set()
    #         for x in toCheck:
    #             for y in lst:
    #                 if x == y:
    #                     return cnt
    #                 if x < y:
    #                     break
    #                 temp.add(x-y)
    #         toCheck = temp
    #
    #     return cnt
    #

        if use_set:
            print(tmp2)
            for element in tmp2:
                for j in range(len(ps)):
                    new_term = term-ps[i]
                    # how to keep track of what ans is?

                    if new_term == 0:
                        return ans

                    elif new_term > 0:
                        new_

        elif use_set == False:
            while ans < n:
                print(ans)
                j = 0
                # print("j: {} len(tmp): {} tmp: {}".format(j, len(tmp), tmp))
                while j < len(tmp):
                    # print("tmp: {}".format(tmp))
                    term = tmp[j]
                    del tmp[j]
                    # print("[after del] tmp: {}".format(tmp))

                    # print("term: {} tmp: {}".format(term, tmp))



                    # j-= 1
                    #
                    # if j == -1:
                    #     j = 0

                    for i in range(len(ps)):
                        # if ps[i] == 4:
                        #     print(term-ps[i])
                        new_term = term-ps[i]

                        if int(new_term) == 0:
                            return ans

                        elif new_term > 0:
                            if new_term not in tmp:
                                tmp.insert(j, new_term)
                                j += 1

                    # print("[after ps itr] tmp: {}\n".format(tmp))

                    # j += 1

                ans += 1




    def numSquares_itr(self, n):
        import math

        if n <= 0:
            return 0

        elif math.sqrt(n) == int(math.sqrt(n)):
            # this only happens when (n)^(1/2) is a whole number
            return 1

        # else, find all perfect squares < n
        ps = [1]

        i = 2
        while i**2 < n:
            ps.append(i**2)
            i += 1

        # test out if ans == 2
        # ans == (number of perfect squares that is required)
        ans = 2
        tmp = [1] * ans

        elem = 0

        while ans < n:

            while elem < len(tmp)-1:
                tmp = []








            ans +=1
            tmp = [0] * ans
            elem = 0

        print("got answer: {}".format(ans))

























        # # define where the last element can be
        # for i in range(0, len(ps)-ans):
        #     tmp[0] = i
        #     placeholder = 1
        #
        #     # initialize elements
        #     tmp[i+1:i+ans]
        #
        #     ...
        #
        #     if sum(tmp) == n:
        #         return ans
        #
        #     tmp = [0] * ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares_dp(15))
