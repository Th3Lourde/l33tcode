'''
Given the root of a binary tree, return the sum or
every node's tilt

The tilt of a tree node is the absolute difference between
the sum of all left subtree node values and all right subtree
node values
'''

from collections import deque

class Solution:
    def findTilt(self, root):
        self.treeTilt = 0

        def dfs(node):
            if not node:
                return 0

            sumLeft = dfs(node.left)
            sumRight = dfs(node.right)

            self.treeTilt += abs(sumLeft - sumRight)

            return node.val + sumLeft + sumRight


        dfs(root)

        return self.treeTilt
