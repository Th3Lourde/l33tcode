'''
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is defined as:
- A binary tree in which left and right subtrees of every node differ in height by
- no more than one

Ok so recursive algo where you find the height of the left subtree,
the height of the right subtree, and if the difference in the height
is greater than one, return false


                1
              2   2
            3  3
           4 4

dfs(1)
    True, 3 = dfs(2)
        True, 2 = dfs(3)
            True, 1 = dfs(4)
            True, 1 = dfs(4)

        True, 1 = dfs(3)
    True, 1 = dfs(2)



'''


class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return True, 0

            validLeft, heightLeft = dfs(node.left)

            validRight, heightRight = dfs(node.right)

            if abs(heightLeft-heightRight) > 1:
                return False, 0

            return validLeft and validRight, max(heightLeft, heightRight) + 1

        resp, _ = dfs(root)

        return resp
