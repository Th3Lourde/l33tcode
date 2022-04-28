class Solution:
    def maxPathSum(self, root):
        self.maxPath = float('-inf')

        def dfs(node):
            valLeft = 0
            valRight = 0

            if node.left:
                valLeft = dfs(node.left)

            if node.right:
                valRight = dfs(node.right)

            self.maxPath = max(self.maxPath, node.val, node.val+valRight, node.val+valLeft, node.val+valRight+valLeft)

            return max(node.val, node.val+valRight, node.val+valLeft)

        dfs(root)
        return self.maxPath
