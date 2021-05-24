'''
        1
     2     3

dfs(1) | 1 + 3, max(1+2+3, 2,3)
    dfs(2) | 2, 2
    dfs(3) | 3, 3

       -10
    9       20
         15    7

dfs(-10) | -1, max(9, 42, -10+9+35)
    dfs(9) | 9, 9
    dfs(20) | 35, max(15, 7, 20+15+7)
        dfs(15) | 15, 15
        dfs(7)  | 7, 7

'''

class Solution:
    def maxPathSum(self, root):
        def dfs(node):
            if not node:
                return float('-inf'),float('-inf')

            maxChildPathSum = float('-inf')
            maxSum = float('-inf')
            sumUsingThisNode = node.val

            # Left Child:
            leftChildPathSum, maxLeftSum = dfs(node.left)

            maxChildPathSum = max(maxChildPathSum, leftChildPathSum)
            maxSum = max(maxSum, maxLeftSum)

            if leftChildPathSum > 0:
                sumUsingThisNode += leftChildPathSum

            # Right Child:
            rightChildPathSum, maxRightSum = dfs(node.right)

            maxChildPathSum = max(maxChildPathSum, rightChildPathSum)
            maxSum = max(maxSum, maxRightSum)

            if rightChildPathSum > 0:
                sumUsingThisNode += rightChildPathSum

            # Check if we only have -inf
            maxChildPathSum = max(0, maxChildPathSum)

            return node.val + maxChildPathSum, max(maxSum, sumUsingThisNode)

        _, maxPath = dfs(root)

        return maxPath
