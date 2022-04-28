# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root: return []

        q = deque([(root, 0)])
        traversal = []

        while q:
            node, level = q.pop()

            if level < len(traversal):
                traversal[level].append(node.val)
            else:
                traversal.append([node.val])

            if node.left:
                q.appendleft((node.left, level+1))

            if node.right:
                q.appendleft((node.right, level+1))

        return traversal
