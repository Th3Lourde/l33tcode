'''
Ok so max width.

Let's create a dict such that we enter in
the level, and get back the min pos and max pos

Let the root node start at pos 0
If we go left, pos = pos -1
If we go right, pos = pos + 1

We care about maximizing the difference in position
for nodes that are on the same level.

We can just maintain a max/min for each level, in order
to do this we would have a nested bfs

Ok so how can we come up with a different mapping?

0

0,1

0,1,2,3

0,1,2,3,4,5,6,7

So it looks like if we go left we mult by 2.
And if we go right we mult by 2 and add 1.

-3 | 1

[0] level = 0
0 --> 0 | pos + 0

[0,0] level = 1
-1 --> 0 | pos + 1
1 --> 1  | pos + 0

[0,0,0,0] level = 2
-2 --> 0 | pos + 2
-1 --> 1 | pos + 2
1 --> 2  | pos + 1
2 --> 3  | pos + 1

[0,0,0,0,0,0,0,0] level = 3
-4 --> 0 | pos + 4
-3 --> 1 | pos + 4
-2 --> 2 | pos + 4
-1 --> 3 | pos + 4
1 --> 4  | pos + 3
2 --> 5  | pos + 3
3 --> 6  | pos + 3
4 --> 7  | pos + 3

Ok so hint, try to come up with a different
way of creating idx's, instead of -1, +1, keep them
all positive
'''

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        q = deque([(root, 0)])
        maxWidth = float('-inf')
        resp = float('-inf')

        while q:
            newQ = deque()
            minPos, maxPos = float('inf'), float('-inf')

            while q:
                node, pos = q.pop()

                minPos = min(minPos, pos)
                maxPos = max(maxPos, pos)

                if node.left:
                    newQ.appendleft((node.left, pos*2))

                if node.right:
                    newQ.appendleft((node.right, pos*2+1))

            # print("{}|{}".format(minPos, maxPos))

            maxWidth = max(maxWidth, maxPos-minPos+1)

            q = newQ

        return maxWidth
