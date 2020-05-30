

class Solution:

    def preorderTraversal(self, root):

        def traverse(node, preOrder):
            if node:
                preOrder.append(node.val)
                traverse(node.left, preOrder)
                traverse(node.right, preOrder)


        preOrder = []

        traverse(root, preOrder)

        return preOrder


    def preorderTraversal_1(self, root): # Iterative
        stack = [root]
        preOrder = []

        while stack:
            node = stack.pop()

            if node:
                preOrder.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

            return preOrder
