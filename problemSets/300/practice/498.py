class Solution:
    def findDiagonalOrder(self, mat):
        ans = []
        end = (len(mat)-1, len(mat[0])-1)
        rows = len(mat)
        cols = len(mat[0])
        r=0
        c=0

        def inBounds(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def goUp(r,c):
            while inBounds(r,c):
                ans.append(mat[r][c])

                if inBounds(r-1, c+1):
                    r -= 1
                    c += 1
                else:
                    break

            if c+1 == cols:
                return r+1, c
            elif r == 0:
                return r, c+1


        def goDown(r,c):
            while inBounds(r,c):
                ans.append(mat[r][c])

                if inBounds(r+1, c-1):
                    r += 1
                    c -= 1
                else:
                    break

            if r+1 == rows:
                return r, c+1
            elif c == 0:
                return r+1, c

        while len(ans) < rows*cols:
            if ((r+c)%2) == 0:
                r,c = goUp(r,c)
            else:
                r,c = goDown(r,c)

        return ans

print(Solution().findDiagonalOrder([[2,3]]))
print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
