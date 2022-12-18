'''
You are climing a staircase, it takes n steps to
reach the top
each time you can take one or two steps forward
How many ways can you reach the top?

cache[n] --> the number of ways you can reach n
'''


class Solution:
    def climbStairs(self, n):
        cache = {1:1, 2:2}

        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]


print(Solution().climbStairs(9))
