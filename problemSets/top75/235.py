'''
Given a binary search tree
find the lowest common ancestor.

So take the path from root --> p,
        path from root --> q,

find the first node that is 'common'
between these two paths.

The easiest way to do this is to find the
first path, make it a set, then when doing the second path
if we hit an intersection point, return that node

'''

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node, path, target):
            path.append(node)

            if node.val == target.val:
                # print(path)
                return True, list(path)

            if node.left:
                found, newPath = dfs(node.left, list(path), target)

                if found:
                    return True, newPath

            if node.right:
                found, newPath = dfs(node.right, list(path), target)

                if found:
                    return True, newPath

            return False, path

        _, pathA = dfs(root, [], p)
        _, pathB = dfs(root, [], q)

        print(pathA)
        print(pathB)

        minPath = pathA
        maxPath = pathB
        minAncestor = None

        if len(pathA) > len(pathB):
            minPath = pathB
            maxPath = pathA

        pathASet = set()

        for node in minPath:
            pathASet.add(node)

        for node in reversed(maxPath):
            if node in pathASet:
                return node
