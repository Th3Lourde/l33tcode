import math

class Solution:

    '''
    I think that this requires some sort
    of number theory in order to get the
    right solution
    '''

    def trailingZeroes(self, n):
        # 1) See if n is divisible by 5

        fives = 0

        while n >= 5:
            if n % 5 == 0:
                fives += math.floor(math.log(n, 5))
            n -= 1

        return fives



    # This works
    def trailingZeroes_1(self, n):
        cnt = 0

        while n > 0:
            cnt += n/5
            n /= 5

        return int(math.floor(cnt))



    def trailingZeroes4(self, n):
        fives = 0

        while n > 1:
            tmp = n

            # print(tmp/5)

            # print(tmp/5 >= 1 and tmp%5 == 0)

            while (tmp/5 >= 1) and (tmp%5 == 0):
                fives += 1
                tmp /= 5
            n -= 1

        return fives



    def trailingZeroes3(self, n):
        fives = 0

        while n > 1:
            goes_in = math.log(n, 5)

            if goes_in % 1 == 0:
                fives += goes_in

            n -= 1

        return fives


    def trailingZeroes2(self, n):
        five = 0
        two = 0

        while n > 1:

            f = "zero"
            t = "zero"

            if n % 5 == 0:
                five += n // 5
                f = n // 5

                tmp = int(n/5)

                # if tmp %



            elif n % 2 == 0:
                two += n // 2
                # two += n / 2
                t = n // 2

            print("n: {} 5: {} 2: {}".format(n, f, t))

            n -= 1

        diff = abs(two-five)

        print("five: {} two: {}".format(five, two))

        # print(five)
        # print(two)

        print(diff)

        if two >= five:
            return two - diff
        elif five > two:
            return five - diff




    def trailingZeroes1(self, n):
        fact = 1

        while n > 1:
            fact *= n
            n -= 1

        trail  = 0

        while fact % 10 == 0:
            trail += 1
            fact =  fact // 10

        return trail


if __name__ == '__main__':
    s = Solution()

    print("Ans: " + str(s.trailingZeroes(30)))
