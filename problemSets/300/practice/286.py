'''
if rooms[r][c] == -1, we are at a wall
if rooms[r][c] == 0, we are at a gate
if rooms[r][c] == 2147483647, we are at an empty room

Fill each empty room with the distance to its nearest gate.

1) Find all gates
bfs for all gates
'''

from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        q = deque()
        empty = 2147483647
        rows = len(rooms)
        cols = len(rooms[0])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0 <= nr < rows and 0 <= nc < cols:
                            q.appendleft((nr,nc,1))

        while q:
            r, c, steps = q.pop()

            if rooms[r][c] == empty:
                rooms[r][c] = steps

                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        q.appendleft((nr,nc,steps+1))

        return rooms
