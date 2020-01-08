
'''
You are climbing a stair case

n steps to reach the top

You can climb up two steps
or one step. There must be
enough steps for you to climb,
however, while this condition
is satisfied, you can either
climb a single step or two
steps, for ever step.

How many distinct ways can you
climb to the top?
'''

class Solution:
    def climbStairs(self, n:int) -> int:

        def n_c_k(n,k):
            import math

            top = math.factorial(n)
            bottom = math.factorial(k)*math.factorial(n-k)

            return top/bottom

        ans = 1
        for i in range(1, (n//2)+1):
            ans += n_c_k(n-i, i)

        return int(ans)



if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
