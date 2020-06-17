# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Check if root exists, return as is appropriate

node = root

if node.val == root: return root

elif node.val < root: node = node.right

elif node.val > root: node = node.left

do while node

if we get outside of while loop, return None


'''


class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        node = root

        while node:
            if node.val == val:
                return node

            elif node.val > val:
                node = node.left

            elif node.val < val:
                node = node.right

        return None
