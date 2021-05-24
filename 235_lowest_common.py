'''
'''

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def search(node, path, target):
            path.append(node)

            if node.val > target:
                search(node.left, path, target)

            elif node.val < target:
                search(node.right, path, target)

        pathP = []
        search(root, pathP, p.val)

        pathQ = []
        search(root, pathQ, q.val)

        idx = 0

        while pathP[idx].val == pathQ[idx].val:
            idx += 1

            if idx >= len(pathP) or idx >= len(pathQ):
                break

        return pathP[idx-1]
