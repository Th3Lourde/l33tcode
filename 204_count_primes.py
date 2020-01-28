
class Solution:

    def countPrimes(self, n): # Slight alteration of previous algo
        def prime(n):
            if n <= 1:
                return False

            i = 2
            while i*i < n: # while i^2 < n, check for prime
                if n%i == 0: return False
                i += 1

            return True

        isPrime = [False, False] + [True]*(n-2)

        for i in range(2, n):
            if isPrime[i]:
                for j in range(i+i, n, i):
                    isPrime[j] = False

        counter = 0
        for num in isPrime:
            if num:
                counter += 1

        return counter


    def countPrimes_2(self, n):
        '''
        Strat: Implement some number-theory algorithm
        that efficiently reveals the number of primes
        that are less than a given prime.

        1) Construct a list to show all possible primes,
        initialize them as being true

        2) march through the list. Every time you find a number
        that is prime, make all factors not prime.

        3) March through the list again and count the number
        of prime numbers
        '''
        def prime(n):
            if n <= 1:
                return False

            i = 2
            while i*i < n: # while i^2 < n, check for prime
                if n%i == 0: return False
                i += 1

            return True


                  # 0, 1 not prime
        isPrime = [False, False] + [True]*(n-2)

        for i in range(n):
            # find number that is prime
            # if we know the number is not
            # prime, skip it.
            if isPrime[i]:
                if prime(i):
                    # find all multiples of that prime number
                    # and set them equal to false (not prime)
                    for j in range(i+i, n, i):
                        isPrime[j] = False



        counter = 0
        for num in isPrime:
            if num:
                counter += 1

        return counter








    def countPrimes_1(self, n):
        '''
        For all elements that are less than n,
        count the number of elements that are
        prime

        The trick here is trying to figure out
        whether or not a number is prime. We could
        store/generate primes less than that number,
        (since a number is prime if (number%2) ^ (number%(any prime)) != 0)

        where we would just iterate through all of the primes, however that
        would take extra time, and it's not obvious that it would be faster
        to do things this way than to just brute-force by checking all odd numbers

        According to the internet, there are a couple of ways of checking to see
        if a number is prime:
            * Is the number even?
            * Is the number divisible by a prime smaller than it?

        Here is my approach:

        loop through all numbers < n.
        record all primes as they are seen.
        if a number is not even, nor divisible by a previously seen prime, it is prime

        All of the solutions use number theory in order to solve it :P

        My solution works, however is not fast enough, due to me not implementing number theory.
        Darn.
        But hey,
        Good news is that I am coming up with solutions to pretty much all of the problems. Just improve
        my ability to implement and we are good to go :)
        '''
        primes = 0
        is_prime = False

        seenPrimes = set()

        if n > 2:
            primes += 1

        for num in range(3, n, 2):
            is_prime =  True

            # we are skipping all even numbers for obvious reasons

            # loop through all previously seen primes, check if num%prime
            for prime in seenPrimes:
                if num%prime == 0:
                    is_prime = False
                    break

            if is_prime:
                primes += 1
                seenPrimes.add(num)


        return primes


if __name__ == '__main__':
    s = Solution()
    # print(s.countPrimes(499979))
    print(s.countPrimes(10))
