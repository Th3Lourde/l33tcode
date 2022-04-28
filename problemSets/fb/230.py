'''
Ok so we could do this via heap
Or
Since it's a BST we could code
up the inOrder traversal and return
the kth node in the travesal
'''

class Solution:
    def kthSmallest(self, root, k):
        self.node_num = 0
        self.ans = None

        def inOrder(node):
            if not node:
                return

            if node.left:
                inOrder(node.left)

            self.node_num += 1

            if self.node_num == k:
                self.ans = node.val

            if node.right:
                inOrder(node.right)

        inOrder(root)

        return self.ans
