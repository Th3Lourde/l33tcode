'''
greatestLength, longest path
'''

class Solution:
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return 0,0

            largestLeft, diam1 = dfs(node.left)
            largestRight, diam2 = dfs(node.right)

            return max(largestLeft+1, largestRight+1), max(diam1, diam2, largestLeft+largestRight)

        length, diam = dfs(root)

        return diam
