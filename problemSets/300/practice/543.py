class Solution:
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return 0,0

            nodesLeft = 0
            maxLeft = 0

            if node.left:
                nodesLeft, maxLeft = dfs(node.left)

            nodesRight = 0
            maxRight = 0

            if node.right:
                nodesRight, maxRight = dfs(node.right)

            return max(nodesRight+1,nodesLeft+1), max(nodesRight+nodesLeft, maxRight, maxLeft)

        _, ans = dfs(root)

        return ans
