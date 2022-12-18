'''
Given root and subRoot, return t/f if
subRoot exists within root.

So perform dfs to find all nodes that have
the same value as subroot.

For each node, perform a bfs traversal to check
if the trees match.

'''

from collections import deque

class Solution:
    def isSubtree(self, root, subRoot):
        self.hits = []

        def dfs(node, target):
            if not node:
                return

            if node.val == target.val:
                self.hits.append(node)

            if node.left:
                dfs(node.left, target)

            if node.right:
                dfs(node.right, target)

        dfs(root, subRoot)

        def isSame(node, targetSubTree):
            q = deque([(node, targetSubTree)])

            while q:
                nodeA, nodeB = q.pop()

                if not nodeA and not nodeB:
                    continue

                if (not nodeA and nodeB) or (nodeA and not nodeB):
                    return False

                elif nodeA.val != nodeB.val:
                    return False

                q.appendleft((nodeA.left, nodeB.left))
                q.appendleft((nodeA.right, nodeB.right))

            return True

        # print(self.hits)

        for hit in self.hits:
            # print(hit)

            if isSame(hit, subRoot):
                return True

        return False
