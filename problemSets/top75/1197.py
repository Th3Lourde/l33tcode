'''
Given an infinite chess board.

The knight starts at [0,0]

Return the minimum number of moves needed for the knight
to reach [x,y].

It is given that the knight can reach [x,y].

So any trends we can think of?

Well the distance between the target and the knight's new
position are some-what related, but this relation can be hard
to see.

A brute force answer would be to have a bfs and a cache. If
the knight lands upon the target, return which iteration we
are on.

Store all positions we have already been to to avoid redundant queries.

Ok, seems that is the one we want
'''

from collections import deque

class Solution:
    def minKnightMoves(self, x, y):
        q = deque([(0,0,0)])
        seen = set({(0,0)})
        x = abs(x)
        y = abs(y)

        while q:
            r,c,steps = q.pop()

            if r == x and c == y:
                return steps

            dirs = [(r-2,c+1),(r-1,c+2),(r+1,c-2),(r+2,c-1),(r+1,c+2),(r+2,c+1)]

            for nr, nc in dirs:
                if (nr, nc) not in seen:
                    seen.add((nr,nc))
                    q.appendleft((nr,nc, steps+1))


class Solution:
    def minKnightMoves(self, x, y):
        q = deque([(0,0)])
        seen = set({(0,0)})
        ans = 0

        while q:
            newQ = deque()

            while q:
                r,c = q.pop()

                if r == x and y == c:
                    return ans

                for nr, nc in [(r-1,c-2),(r-2,c-1),(r-2,c+1),(r-1,c+2),(r+1,c-2),(r+2,c-1),(r+1,c+2),(r+2,c+1)]:
                    if (nr, nc) not in seen:
                        seen.add((nr,nc))
                        newQ.appendleft((nr,nc))

            ans += 1
            q = newQ
