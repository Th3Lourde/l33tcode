'''
Given an integer n, return true if it is a power of two.
Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

2
4
8

8=

We can just divide by two until we get one.

Divide by two. If answer is even, divide by two again.
else, if answer is 1, return True
else: return False

log(n), b/c we are halving the size of the number every time



'''

20+15

2 // 2
4 // 2
6 // 2
8 // 2
16 // 2

class Solution:
    def isPowerOfTwo_1(self, n):
        if n == 0:
            return False

        while n % 2 == 0:
            n = int(n/2)

        if n == 1:
            return True

        return False

        # This is slower than the first solution 
    def isPowerOfTwo(self, n):
        if n == 0:
            return False

        if n == 1:
            return True

        l = 1
        r = n

        while l < r:
            m = (l+r)//2

            if 2**m < n:
                l = m+1
            else:
                r = m

        return 2**l == n

print(Solution().isPowerOfTwo(0))
print(Solution().isPowerOfTwo(2))
print(Solution().isPowerOfTwo(6))
print(Solution().isPowerOfTwo(7))
print(Solution().isPowerOfTwo(8))
