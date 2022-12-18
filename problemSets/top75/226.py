'''

'''

class Solution:
    def invertTree(self, root):
        def invert(node):
            if not node:
                return None

            node.left, node.right = node.right, node.left

            invert(node.left)
            invert(node.right)

        invert(root)
        return root
