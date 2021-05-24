'''
Perform inOrderTraversal,
once traversal is of length
K, return last element in traversal.
'''

class Solution:
    def kthSmallest(self, root, k):
        def inOrder(node, traversal):
            if not node:
                return

            inOrder(node.left, traversal)

            if len(traversal) < k:
                traversal.append(node.val)

            if len(traversal) < k:
                inOrder(node.right, traversal)

        inOrderTraversal = []

        inOrder(root, inOrderTraversal)

        return inOrderTraversal[-1]
