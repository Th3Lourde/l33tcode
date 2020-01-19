
class Solution:
    def countPrimes(self, n):
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
    print(s.countPrimes(499979))
