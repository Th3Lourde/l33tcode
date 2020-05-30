
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root): # iterative
        stack = [root]
        inOrder = []

        while stack:
            node = stack.pop()

            if node:
                if type(node) == type(5):
                    inOrder.append(node)

                else:
                    stack.append(node.right)
                    stack.append(node.val)
                    stack.append(node.left)

        return inOrder

    def inorderTraversal_1(self, root): # recursive
        def traverse(node, inOrder):
            if node:
                traverse(node.left, inOrder)
                traverse(node.right, inOrder)
                inOrder.append(node.val)

        inOrder = []

        traverse(root, inOrder)

        return inOrder
