
'''
PASS
[
[1,1,1],
[0,0,0],
[0,1,1]
]

[ [1,1,1], [0,0,0], [0,1,1] ]

[
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,1,0,0,0,0,0],
[0,1,1,0,0,0,0]
]

[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0]
]

[
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,1,0,0,0,0,0],
[0,1,1,0,0,0,0]
]

'''

class Solution:
    # Too slow
    def shortestBridge_1(self, grid):
        def bfs(row, col):
            visited = set()
            q = deque([(row,col)])

            while q:
                row, col = q.popleft()

                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    if grid[row][col] == 1:
                        visited.add((row,col))

                        for l,r in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nRow = row+l
                            nCol = col+r

                            if (nRow,nCol) not in visited:
                                q.append((nRow,nCol))

            return visited

        def getTwoIslands():
            setA = set()
            setB = set()

            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1 and (row, col) not in setA and (row, col) not in setB:
                        if len(setA) == 0:
                            setA = bfs(row, col)
                        else:
                            setB = bfs(row, col)

            return setA, setB

        setA, setB = getTwoIslands()

        # Set all of setA to -1
        for i,j in setA:
            grid[i][j] = -1

        # print(setA)
        # print(setB)
        step = 0

        while True:
            new = []

            print(setA)

            for i,j in setA:
                for nR, nC in [(0,1), (0,-1), (1,0), (-1,0)]:
                    row = i+nR
                    col = j+nC

                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                        if grid[row][col] == 1:
                            print("{},{}".format(row, col))
                            return step

                        elif grid[row][col] == 0:
                            grid[row][col] = -1
                            new.append((row,col))

            step += 1
            setA = new


    def shortestBridge(self, grid):
        # 1 Find the first island
        # 2 Find all land in the first island
        # |--> mark all land as -1
        # 3 Perform bfs on all of the land, looking for the next island
        islandA = set()
        itr = [(0,1), (0,-1), (-1,0), (1,0)]

        def findFirst():
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1:
                        return row, col

        def dfs(row, col):
            islandA.add((row, col))
            grid[row][col] = -1

            for nr, nc in itr:
                nRow = row + nr
                nCol = col + nc

                if 0 <= nRow < len(grid) and 0 <= nCol < len(grid[0]) and grid[nRow][nCol] == 1:
                    islandA.add((nRow, nCol))
                    dfs(nRow, nCol)


        row, col = findFirst()
        dfs(row, col)

        print(islandA)

        steps = 0

        while islandA:
            new = []

            for row, col in islandA:
                for nr, nc in itr:
                    nRow, nCol = row+nr, col+nc

                    if 0 <= nRow < len(grid) and 0 <= nCol < len(grid[0]):
                        if grid[nRow][nCol] == 1:
                            return steps

                        elif grid[nRow][nCol] == 0:
                            grid[nRow][nCol] = -1
                            new.append((nRow, nCol))

            steps += 1
            islandA = new



print(Solution().shortestBridge([[0,0,0,1,1,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,1,1,0,0,0,0]]))

print(Solution().shortestBridge([ [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,1,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,1,0,0,0,0] ]))
