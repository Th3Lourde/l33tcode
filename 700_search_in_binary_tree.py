# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Given a root of a binary tree
and a target value

Find and return the node with a value of val
If such a node does not exist, return None
'''

from collections import deque

class Solution:
    def searchBST(self, root, val):
        if root == None:
            return None

        q = deque([root])

        while q:
            node = q.pop()

            if node.val == val:
                return node

            if node.left:
                q.appendleft(node.left)

            if node.right:
                q.appendleft(node.right)

        return None
