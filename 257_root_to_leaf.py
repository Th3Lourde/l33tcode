# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

bfs, (node, path)
once node reaches end add path to a list


'''
from collections import deque

class Solution:
    def binaryTreePaths(self, root):
        paths = []

        if not root:
            return paths

        q = deque({(root, "{}".format(root.val))})

        while q:
            node, path = q.pop()

            if node.left:
                q.appendleft((node.left, path + "->{}".format(node.left.val)))

            if node.right:
                q.appendleft((node.right, path + "->{}".format(node.right.val)))

            if not node.left and not node.right:
                paths.append(path)


        return paths
