'''
Count the number of prime numbers less than a non-negative number

these number theory questions are fun :)

count up to the number. Every time you encounter a prime,
store it. If you are not sure if the number is prime,
check if it is divisible by the primes you have encountered
so far. If it is not, it is a prime
'''

class Solution:

    def countPrimes(self, n):
        isPrime = [0,0] + [True]*(n-2)

        i = 2
        while i*i < n:
            if (not isPrime[i]):
                for j in range(i*i, n, i):
                    isPrime[j] = False
            i += 1

        count = 0
        for i in range(2, n):
            if (isPrime[i]):
                count += 1

        return count

        # this is an approximation, not the actual value :/
    def countPrimes_2(self, n):
        import math

        return int(n/math.log1p(n))

    # too slow :/
    def countPrimes_1(self, n):

        if n <= 1:
            return 0


        primes = [2]

        for i in range(3, n):
            isPrime = True

            for prime in primes:
                if i % prime == 0:
                    isPrime = False

            if isPrime:
                primes.append(i)

        return len(primes)




if __name__ == '__main__':
    s = Solution()

    print(s.countPrimes(10))
