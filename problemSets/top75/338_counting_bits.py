'''
Given an integer n,
return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Ok so we are given an integer.
Return an array length of integer + 1.

arr[i] equals the number of ones in the binary representation of that number.

Looking at the first 10 numbers we can notice a pattern.
If the number is even:
    --> Go to the number / 2 and add a zero?

If the number is odd:
    - Go to last even number and add one.

'''

def firstN(n):
    for i in range(n+1):
        print("{} --> {}".format(i, bin(i)))

firstN(10)

class Solution:
    def countBits(self, n):
        if n < 2:
            return [i for i in range(n+1)]

        # binary_terms = [0, 1, 1]
        dp = [0, 1, 1]

        for i in range(3, n+1):
            if i % 2 == 0:
                # prevTerm = binary_terms[i/2]
                # binary_terms.append(prevTerm << 1)
                dp.append(dp[int(i/2)])
            else:
                # binary_terms.append(binary_terms[i-1]+1)
                dp.append(dp[i-1]+1)

        return dp

def countOnes(n):
    ans = 0

    while n:
        ans += n&1
        n >>= 1

    return ans

print(countOnes(7))


print(bin(3))

print(Solution().countBits(5))
