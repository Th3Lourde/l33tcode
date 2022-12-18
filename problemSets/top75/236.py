class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node, path, target):
            if not node:
                return []

            if node.val == target:
                return path+[node]

            pathLeft = dfs(node.left, path+[node], target)

            if pathLeft:
                return pathLeft

            pathRight = dfs(node.right, path+[node], target)

            if pathRight:
                return pathRight

            return []

        pathA = dfs(root, [], p.val)
        pathB = dfs(root, [], q.val)

        # print(pathA)
        # print(pathB)

        i = 0
        n = min(len(pathA), len(pathB))

        while i+1 < n and pathA[i+1].val == pathB[i+1].val:
            i += 1

        return pathA[i]
