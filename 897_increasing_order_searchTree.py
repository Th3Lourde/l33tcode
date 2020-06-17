'''
Given the root of a binary search tree.
Return the tree in a fashion s.t. it is in
written in a linked list fashion (populate the right child)

'naive algo':

get the pre order (store the nodes instead of the val)

Loop through the inOrder, reset each node and point the right
to the next node
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        pre = []

        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if type(node) == type(['1']):
                    pre.append(node[0])

                elif type(node) != type(['1']):
                    stack.append(node.right)
                    stack.append([node])
                    stack.append(node.left)


        for i in range(len(pre)-1):
            pre[i].left = None
            pre[i].right = pre[i+1]

        pre[-1].left = None
        pre[-1].right = None

        return pre[0]
