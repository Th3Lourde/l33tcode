
class Solution:
    def numSquares(self, n):
        import math

        if n <= 0:
            return 0

        elif math.sqrt(n) == int(math.sqrt(n)):
            return 1

        elif n == 2:
            return 2

        elif n == 3:
            return 3

        ps = []
        tmp2 = set()

        for i in range(1, n):
            if i**2 < n:
                ps.append(i**2)
                tmp2.add(n - i**2)

            elif i**2 > n:
                break

        paths = {n}
        ans = 0

        while paths:
            tmp = set()
            ans += 1

            for element in paths:
                for edge in ps:
                    if element - edge == 0:
                        return ans

                    elif element - edge > 0:
                        tmp.add(element-edge)
            paths = tmp









if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(7168))
