# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root):
        inOrderArr = []

        def inOrder(node):
            if node.left:
                inOrder(node.left)

            inOrderArr.append(node)

            if node.right:
                inOrder(node.right)


        inOrder(root)

        swap = []

        inOrderVals = []

        for node in inOrderArr:
            inOrderVals.append(node.val)

        inOrderVals.sort()

        for idx in range(len(inOrderVals)):
            if inOrderArr[idx].val != inOrderVals[idx]:
                swap.append(inOrderArr[idx])

        swap[0].val, swap[1].val = swap[1].val, swap[0].val
