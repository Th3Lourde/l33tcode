# for (nr, nc) in [(r + 1,c), (-1,0), (0,1), (0,-1)]:
#   newX, newY = x+dirr[0], y+dirr[1]
#   if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 and (newX, newY) not in visited:
#           matrix[newX][newY] = matrix[x][y] + 1
#           visited.add((newX, newY))
#           q.append((newX, newY))

'''
Ok so the answer is to do bfs. The question that I had for this
is about how we manage the queries and stop querying once we have
our answer.

bfs via stack.

Current idea:
Fill the stack with the coordinates
of every one in the matrix.

Then create an empty matrix.

The question that I have is how do we
know what position to write to?

So I was right! (later)

Do a bfs on the zeros, and write to the values
that don't have any zeroes.

Let's also use deque b/c practice

1) Store the row/column of every element whose value is zero
2) Create a new matrix with all values initialized as -1
3) Pop from right, if element == -1, write depth to element
4) For every valid neighbor, push the coords and the new depth.
5) Continue until stack is empty

We can avoid using a set if we simply use the min. We know
number of elements doesn't exceed 10k. I would rather use
float('inf').



'''
import collections
class Solution:
    def updateMatrix(self, matrix):
        R, C = len(matrix), len(matrix[0])

        def neighbors(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        q = collections.deque([( (r,c), 0)
                    for r in range(R)
                    for c in range(C)
                    if matrix[r][c] == 0])

        resp = [[float('inf') for _ in range(C)] for _ in range(R)]

        while q:
            (r, c), depth = q.popleft()

            if depth < resp[r][c]:
                resp[r][c] = depth
            else:
                continue

            for nei in neighbors(r, c):
                q.append((nei, depth+1))

        return resp









    # DFS is too slow
    def updateMatrix_1(self, matrix):
      seen = [set()]

      def dfs(row, col):
        # print("Call row:{} | col:{}".format(row, col))
        # given that we are in bounds
        if matrix[row][col] == 0:
          return 0


        minDist = float('inf')

        seen[0].add((row,col))

        for nr, nc in [(row,col-1), (row, col+1), (row+1,col), (row-1,col)]:
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                # print(seen)
                # print("")

                if (nc, nc) not in seen[0]:
                    minVal = dfs(nr,nc)+1
                else:
                    minVal = matrix[nr][nc]+1

                minDist = min(minDist, minVal)

                if minDist == 1:
                    break

                # minDist = min(minDist, matrix[nr][nc] if (nr,nc) in seen[0] else dfs(nr, nc , 0)+1)

        matrix[row][col] = minDist

        return minDist

      for row in range(len(matrix)):
        for col in range(len(matrix[0])):
          if matrix[row][col] == 0 or (row, col) in seen[0]:
            continue

          # print("row: {}, col: {}".format(row, col))
          minVal = dfs(row, col)

      return matrix

# input = [[0,0,0],
#          [0,1,1],
#          [1,1,1]]

# input = [[0,1,1],
#          [1,1,1],
#          [1,1,1]]

# input = [[1,1,1], [1,1,1], [1,1,0]]
input = [[1,0,0], [0,0,0], [1,1,0]]
s = Solution()
print(s.updateMatrix(input))

# https://leetcode.com/problems/01-matrix/
