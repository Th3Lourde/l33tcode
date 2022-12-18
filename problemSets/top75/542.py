'''
Given a binary matrix, return the nearest 0 for each cell.

So for every one, perform a bfs to find the nearest zero.

So 0(n)*(number of ones)


[0,1,0,1,1],
[1,1,0,0,1],
[0,0,0,1,0],
[1,0,1,1,1],
[1,0,0,0,1],

'''

# class Solution:
#     def updateMatrix(self, mat):
#         rows = len(mat)
#         cols = len(mat[0])
#         solved = {}
#
#         def itr(r,c, path):
#             if (r,c) in solved:
#                 return solved[(r,c)]
#
#             if mat[r][c] == 0:
#                 return 0
#
#             ans = float('inf')
#
#             for nr, nc in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
#                 if 0 <= nr < rows and 0 <= nc < cols:
#                     if (nr,nc) not in path:
#                         path.add((nr,nc))
#                         ans = min(ans, itr(nr, nc, path)+1)
#                         path.remove((nr,nc))
#
#             solved[(r,c)] = ans
#             return ans
#
#         for r in range(rows):
#             for c in range(cols):
#                 if mat[r][c] != 0:
#                     mat[r][c] = itr(r,c,set({(r,c)}))
#
#         return mat


from collections import deque

class Solution:
    def updateMatrix(self, mat):
        zeroes = deque([])
        rows = len(mat)
        cols = len(mat[0])
        solved = set()
        d = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    zeroes.appendleft((r,c))

        while zeroes:
            new_zeroes = deque([])
            d += 1

            while zeroes:
                r,c = zeroes.pop()

                for nr, nc in [(r+1, c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if mat[nr][nc] != 0 and (nr, nc) not in solved:
                            mat[nr][nc] = d
                            solved.add((nr, nc))
                            new_zeroes.appendleft((nr,nc))

            zeroes = new_zeroes

        return mat






print(Solution().updateMatrix([[1,1,1], [1,1,0], [1,1,1]]))
