'''
Given the root of a binary search tree and a node
in the binary tree,

Return the next node that is greater than the node that
we have

Ok so the next greater node is either the root, the left most
of the next subtree on the right, or the node on the right.

It would just be easier to get the inOrder traversal of the tree
and return the node after p.val

'''

class Solution:
    def inorderSuccessor(self, root, p):
        traversal = []

        def inOrder(node):
            if not node:
                return

            if node.left:
                inOrder(node.left)

            traversal.append(node)

            if node.right:
                inOrder(node.right)

        inOrder(root)

        for idx, node in enumerate(traversal):
            if node.val != p.val:
                continue

            if idx == len(traversal)-1:
                return None

            return traversal[idx+1]
