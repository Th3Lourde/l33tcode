'''
For every idx, we have the choice to jump left or right.
We don't know which one will result in the 'correct' solution,
so we should perform both jumps.

We should also have a visited set so we don't follow the same path
multiple times

Add to set when we add to the queue

use bfs to return the first correct traversal
start = 5

0 1 2 3 4 5 6
-------------
4,2,3,0,3,1,2
  ^


visited = {1,4,5,6}
q = []

1

return True

'''

from collections import deque

class Solution:
    def canReach(self, arr, start):
        visited = set({start})
        q = deque([start])

        def inBounds(idx):
            return 0 <= idx < len(arr)

        while q:
            idx = q.pop()

            if arr[idx] == 0:
                return True

            moveRight = idx + arr[idx]

            if inBounds(moveRight) and moveRight not in visited:
                visited.add(moveRight)
                q.appendleft(moveRight)

            moveLeft = idx - arr[idx]

            if inBounds(moveLeft) and moveLeft not in visited:
                visited.add(moveLeft)
                q.appendleft(moveLeft)

        return False

print(Solution().canReach([4,2,3,0,3,1,2], 5))
print(Solution().canReach([4,2,3,0,3,1,2], 0))
print(Solution().canReach([3,0,2,1,2], 2))
