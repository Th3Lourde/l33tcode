


class Solution:
    def arrangeCoins(self, n):
        i = 1
        ans = 0

        while True:
            n -= i

            if n >= 0:
                ans += 1

            elif n < 0:
                return ans


            i += 1


if __name__ == '__main__':
    s = Solution()

    print(s.arrangeCoins(5))
