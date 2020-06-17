# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Return True if every value in the tree is the
same. Else False.
'''


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        compare = root.val
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if node.val != compare: return False

                stack.append(node.right)
                stack.append(node.left)

        return True
