'''
Ok, so how could we make this faster?

One thing that we have done is that we check
everything around us. Would it be possible to
only check in a single direction?

One idea would be to check all surrounding squares,
increasing by an order of magnitude for each check.

The first time we see a one, stop, iterate through
all of the ones and record the shortest distance.

We would know the number of times that we could do
this based on the position of the square.

Another idea could be, every time we see a one,
to locate all zeros one square away and record the
one as the closest piece of land around.





'''

class Solution:

    def maxDistance(self, grid):
        m,n = len(grid), len(grid[0])
        q = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        if len(q) == n*m or len(q) == 0: return -1

        level = 0

        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.pop()

                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xi, yj = x+i, y+j

                    if 0 <= xi < n and 0 <= yj < m and grid[xi][yj] == 0:
                        q.insert(0, (xi, yj))
                        grid[xi][yj] = 1

            level += 1
        return level-1


    # TLE
    def maxDistance_i(self, grid):

        def isValid(point):
            if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0]):
                return True
            return False

        def itr(row, col):

            seen = set()

            pos = [
                (0,1),
                (0,-1),
                (1,0),
                (-1,0),
            ]

            q = [ [(row, col), 0] ]

            while q:

                # [ (row, col), distTraveled ]
                node = q.pop()

                if grid[node[0][0]][node[0][1]] == 1:
                    return node[1]

                seen.add(node[0])

                for p in pos:
                    step = (node[0][0]+p[0], node[0][1]+p[1])

                    if step not in seen and isValid(step):
                        q.insert(0, [step, node[1]+1])

            return -1

        ans = -1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    ans = max(ans, itr(row, col))

        return ans
