'''
Given the root of a binary tree, return its maximum depth.

'''

class Solution:
    def maxDepth(self, root):
        self.maxDepth = float('-inf')

        if not root:
            return 0

        def dfs(node, depth):
            if node.left:
                dfs(node.left, depth+1)

            if node.right:
                dfs(node.right, depth+1)

            self.maxDepth = max(self.maxDepth, depth)

        dfs(root, 1)

        return self.maxDepth
