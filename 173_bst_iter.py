# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root):
        def inOrder(node, traversal_list):

            if node.left:
                inOrder(node.left, traversal_list)

            traversal_list.append(node.val)

            if node.right:
                inOrder(node.right, traversal_list)

        inorder_traversal = []

        inOrder(root, inorder_traversal )

        print(inorder_traversal)

        self.travesal = inorder_traversal
        self.idx = -1

    def next(self):
        self.idx += 1
        return self.travesal[self.idx]

    def hasNext(self):
        return self.idx < len(self.travesal)-1
