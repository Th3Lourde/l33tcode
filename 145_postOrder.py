
class Solution:
    def postorderTraversal(self, root): # iterative solution
        stack = [root]
        postOrder = []

        while stack:
            node = stack.pop()

            if node:
                if type(node) == type(5):
                    postOrder.append(node)

                else:
                    stack.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)

        return postOrder

    def postorderTraversal(self, root): # recursive solution

        def traverse(node, postOrder):
            if node:
                traverse(node.left, postOrder)
                traverse(node.right, postOrder)
                postOrder.append(node.val)

        postOrder = []

        traverse(root, postOrder)

        return postOrder
