
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
import math

class Solution:
    def climbStairs_1(self, n:int) -> int:

        def n_c_k(n,k):
            import math

            top = math.factorial(n)
            bottom = math.factorial(k)*math.factorial(n-k)

            return top/bottom

        ans = 1
        for i in range(1, (n//2)+1):
            ans += n_c_k(n-i, i)

        return int(ans)

    def climbStairsOld(self, n):
        ans = 1
        twos = n//2
        ones = n%2

        def nCk(n, k):
            if n == 2 and k == 1:
                return 1

            return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


        while twos >= 0:
            # print("[{} | {}]".format(ones, twos))
            if ones == 0:
                twos -= 1
                ones += 2
                continue


            ans += nCk(twos+ones, min(ones, twos))

            twos -= 1
            ones += 2

        return int(ans)

    def climbStairs(self, n):
        dp = [1, 1]

        for i in range(2, n+1):
            dp.append(dp[i-1]+dp[i-2])

        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs(2))
    print(s.climbStairs(4))
    print(s.climbStairs(5))
