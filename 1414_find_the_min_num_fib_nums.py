'''
Find the min numb of fib nums
whose sum is K.

So we have this number, we want
to know how many fib numbers are required
to create the sum of that number.

1) Generate all fib <= K
2) subtract the max num from K, update cntr, continue
3) continue until done

k = 7

lookingFor = 7

            # stop at 8 b/c > 7
fibs = set({1,1,2,3,5,8})

currentFib = 8

if currentFib > k:
    currentFib = findNextLowestFib(currentFib)

def findNextLowestFib(n):

    if n < 1:
        print("Error")
        return 0

    # n -= 1 until is fib

ans = 0

while lookingFor > 0:
    # Assuming currentFib < lookingFor

    lookingFor -= currentFib
    ans += 1

    currentFib = findNextLowestFib(lookingFor)

return ans

What if we put all of the fibs in a list,
and also have a dict with their index?

Then we don't need to -= 1

Solution is right, just too slow.



'''

class Solution:
    def findMinFibonacciNumbers(self, k):

        lookingFor = k

        def generateFibs(k, fibs):
            if k <= 1:
                return fibs

            f1 = 1
            f2 = 1

            while f1+f2 <= k:
                fn = f1+f2

                fibs.append(fn)

                f1 = f2
                f2 = fn

            return fibs

        fibs = generateFibs(k, [0, 1])

        currentFib = fibs[-1]
        i = len(fibs)-1

        ans = 0

        while lookingFor > 0:

            lookingFor -= currentFib
            ans += 1

            while fibs[i] > lookingFor:
                i -= 1

            currentFib = fibs[i]

        return ans


if __name__ == '__main__':
    sol = Solution()

    print(sol.findMinFibonacciNumbers(1))
    print(sol.findMinFibonacciNumbers(7))
    print(sol.findMinFibonacciNumbers(10))
    print(sol.findMinFibonacciNumbers(19))

    # TLE 645157245
