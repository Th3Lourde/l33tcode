class Solution:
    def uniquePaths(self, m, n):
        cache = {}

        for r in range(0, m):
            for c in range(0, n):
                if r == 0 and c == 0:
                    cache[(r,c)] = 1

                else:
                    resp = 0

                    if r-1 >= 0:
                        resp += cache[(r-1,c)]

                    if c-1 >= 0:
                        resp += cache[(r, c-1)]

                    cache[(r,c)] = resp

        # print(cache)

        return cache[(m-1, n-1)]



print(Solution().uniquePaths(3,2))
print(Solution().uniquePaths(3,7))
