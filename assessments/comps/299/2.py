'''
So we are just supposed to do a few and see
that it is the fib sequence. Fun.

Ok so let's redo this question with the knowledge
that this is a fib question

f_n = f_(n-1) + f_(n-2)

'''



class Solution:
    def countHousePlacements(self, n):
        mod = 10 ** 9 + 7
        prev, curr = 1, 1

        for _ in range(n):
            new_curr = (prev+curr) % mod
            prev, curr = curr, new_curr

        return (curr ** 2) % mod


print(Solution().countHousePlacements(1))
print(Solution().countHousePlacements(2))
print(Solution().countHousePlacements(3))
print(Solution().countHousePlacements(4))
print(Solution().countHousePlacements(64))
