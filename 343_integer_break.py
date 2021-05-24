class Solution:
    # Top-Down
    def integerBreak_1(self, n):
        cache = {0:1, 1:1, 2:1}

        def itr(n):
            if n < 2: return 1
            if n in cache: return cache[n]

            max_prod = float('-inf')

            n1 = 1
            n2 = n-1
            while n1 <= n2:
                # print("Spliting {} into {}+{}".format(n,n1,n2))
                max_prod = max(max_prod, itr(n1)*itr(n2))
                max_prod = max(max_prod, n1*itr(n2))
                max_prod = max(max_prod, itr(n1)*n2)
                max_prod = max(max_prod, n1*n2)
                n1 += 1
                n2 -= 1

            cache[n] = max_prod
            return cache[n]

        return itr(n)

    def integerBreak(self, n):
        dp = [1,1]

        for i in range(2, n+1):
            l = 1
            r = i-1
            max_prod = float('-inf')

            while l <= r:
                max_prod = max(max_prod, l*r, dp[l]*r, l*dp[r], dp[l]*dp[r])
                l += 1
                r -= 1

            dp.append(max_prod)

        # print(dp)

        return dp[n]

if __name__ == '__main__':
    s = Solution()

    print(s.integerBreak(3))
    print(s.integerBreak(5))
    print(s.integerBreak(58))

'''
3 | 2
5 | 6
8 | 18


'''
