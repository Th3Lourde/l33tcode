'''

Ok so we have multiple islands. We want to find
the maximum gold that we can get from visiting
the different islands.

The problem is easy/correct when there is only one
island. The problem is not easy/correct when there
are multiple islands.

When we visit an island, we want to return the maximum
gold that we can get from the island, as well as the
different positions that make up the island.

Every time we see a position that doesn't belong to an
island that we have already been to, run the path finding
algorithm on it and return the max gold/nodes that make
up that island.

Ok so I don't 100% understand why my algo doesn't work,
however I know that the other dude's does.

Let's just use his algorithm.

No, let's learn why ours doesn't work.

What are some of the assumptions that we are making in our
code?

One of the assumptions that we are making is that we can
visit multiple islands, and bring that gold that we find
along with us.

Or that the different islands that we are visiting as a
part of our journey are disjoint.

Ok yea let's just move on. This dude has a super clean
solution. Let's just use it and continue. We've been at
this for a couple of hours.

        def maxPath(i, j):
            gold = 0

            v = set()

            stack = [[ i, j, grid[i][j], set() ]]

            while stack:
                # Location will only be equal to valid idx whose val != 0
                loc = stack.pop()

                v.add((loc[0], loc[1]))

                if (loc[0], loc[1]) in loc[3]:
                    continue
                else:
                    loc[3].add((loc[0], loc[1]))

                gold = max(gold, loc[2])

                if loc[0] > 0 and grid[loc[0]-1][loc[1]] != 0:
                    stack.append([ loc[0]-1, loc[1], loc[2] + grid[loc[0]-1][loc[1]], loc[3] ])

                if loc[0] < len(grid)-1 and grid[loc[0]+1][loc[1]] != 0:
                    stack.append([ loc[0]+1, loc[1], loc[2] + grid[loc[0]+1][loc[1]], loc[3]  ])

                if loc[1] > 0 and grid[loc[0]][loc[1]-1] != 0:
                    stack.append([ loc[0], loc[1]-1, loc[2] + grid[loc[0]][loc[1]-1], loc[3]  ])

                if loc[1] < len(grid[0])-1 and grid[loc[0]][loc[1]+1] != 0:
                    stack.append([ loc[0], loc[1]+1, loc[2] + grid[loc[0]][loc[1]+1], loc[3]  ])

            return gold, v



class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0

        def maxPath(i, j):
            grid[i][j] *= -1

            max_path = 0

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                if (0  <= i+dr < len(grid)) and (0 <= j+dc < len(grid[0])):
                    if grid[i+dr][j+dr] > 0:
                        max_path = max(max_path, maxPath(i+dr, j+dc))

            grid[i][j] *= -1
            return grid[i][j] + max_path

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    g = maxPath(i, j)
                    ans = max(ans, g)

        return ans






'''

class Solution:
    def getMaximumGold(self, grid):
        ans = 0

        def maxPath(i, j):
            grid[i][j] *= -1

            max_path = 0

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                if (0  <= i+dr < len(grid)) and (0 <= j+dc < len(grid[0])):
                    if grid[i+dr][j+dc] > 0:
                        max_path = max(max_path, maxPath(i+dr, j+dc))

            grid[i][j] *= -1
            return grid[i][j] + max_path

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    g = maxPath(i, j)
                    ans = max(ans, g)

        return ans
