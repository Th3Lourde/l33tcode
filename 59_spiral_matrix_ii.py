class Solution:
    def generateMatrix(self, n):
        m = [[0 for _ in range(n)] for _ in range(n)]
        i,j,c = 0,0,1

        if n == 1: return [[1]]

        def t(i,j,c):
            # print("i:{}|j:{}|c:{}".format(i,j,c))
            while j < n and m[i][j] == 0:
                m[i][j] = c
                j += 1
                c += 1

            return i+1, j-1, c

        def r(i,j,c):
            # print("i:{}|j:{}|c:{}".format(i,j,c))
            while i < n and m[i][j] == 0:
                m[i][j] = c
                i += 1
                c += 1

            return i-1, j-1, c

        def b(i,j,c):
            # print("i:{}|j:{}|c:{}".format(i,j,c))
            while j >= 0 and m[i][j] == 0:
                m[i][j] = c
                j -= 1
                c += 1

            return i-1, j+1, c

        def l(i,j,c):
            # print("i:{}|j:{}|c:{}".format(i,j,c))
            while i >= 0 and m[i][j] == 0:
                m[i][j] = c
                i -= 1
                c += 1

            return i+1, j+1, c


        while m[i][j] == 0:
            # print(m)
            i,j,c = t(i,j,c)
            # print(m)
            i,j,c = r(i,j,c)
            # print(m)
            i,j,c = b(i,j,c)
            # print(m)
            i,j,c = l(i,j,c)

        return m

s = Solution()

print(s.generateMatrix(3))
print(s.generateMatrix(1))
