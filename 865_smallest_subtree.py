'''
So the goal here is to find the smallest subtree that contains
all of the deepest nodes.

An easy way to do this is to find the deepest nodes, the path to
the deepest nodes, and then find the first node that they all have
in common. Since they all have the same depth, we can just move backwards
until we find our match.

So, we can just take any two nodes and do this to the path.

bfs to create a mapping from depth to path

            3
          5   1
         6 2 0  8
          7 4

(node, path)

Add to dict once we pop from queue


q = []

q = []
(3, [])
depthToPaths = {1: (3), 2: [(3,5), (3,1)]}


'''

from collections import deque

class Solution:
    def subtreeWithAllDeepest(self, root):
        q = deque([(root, [])])
        depthToPaths = {}
        maxDepth = 0

        while q:
            node, path = q.popleft()

            # Update path
            path = list(path) + [node]

            # Calc depth, update maxDepth
            depth = len(path)
            maxDepth = max(maxDepth, depth)


            if depth in depthToPaths:
                depthToPaths[depth].append(path)
            else:
                depthToPaths[depth] = [path]

            # Add children to q
            if node.left:
                q.append((node.left, path))

            if node.right:
                q.append((node.right, path))

        # Now go to max depth, get the nodes of max depth
        # If there is one node, return the node
        # If there are multiple nodes, return the first common (start from rhs)

        paths = depthToPaths[maxDepth]

        if len(paths) == 1:
            return paths[0][-1]

        ptr = len(paths[0])
        matches = False
        tmp = None

        while matches == False:
            matches = True
            ptr -= 1

            for idx in range(len(paths)):
                if idx == 0:
                    tmp = paths[idx][ptr]
                elif paths[idx][ptr] != tmp:
                    matches = False
                    break

        return paths[0][ptr]
