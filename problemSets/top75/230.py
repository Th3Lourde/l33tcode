'''
So if we get the in-order traversal of the tree,
the kth element of the traversal is what we are looking for
'''

class Solution:
    def kthSmallest(self, root, k):
        traversal = []

        def inOrder(node):
            if not node:
                return

            if node.left:
                inOrder(node.left)

            traversal.append(node.val)

            if node.right:
                inOrder(node.right)

        inOrder(root)

        return traversal[k-1]
