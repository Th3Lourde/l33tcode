'''
P and q are nodes in a tree root.
Each node has a path, which is the series of nodes that must
be traversed in order to reach that node.
Find the first path node that p and q have in common
'''

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node, path, target):
            if not node:
                return False

            if node.val == target:
                path.append(node)
                return True

            if node.left:
                path.append(node)
                if dfs(node.left, path, target):
                    return True
                path.pop()

            if node.right:
                path.append(node)
                if dfs(node.right, path, target):
                    return True
                path.pop()

            return False

        pathP = []
        dfs(root, pathP, p.val)

        pathQ = []
        dfs(root, pathQ, q.val)

        traversePath = pathP
        traverseSet = pathQ

        if len(pathP) > len(pathQ):
            traversePath = pathQ
            traverseSet = pathP

        valSet = set()

        for node in traverseSet:
            valSet.add(node.val)

        matches = []

        for node in traversePath:
            if node.val in valSet:
                matches.append(node)

        return matches.pop()
