from collections import deque

class Solution:
    def rangeSumBST(self, root, low, high):
        q = deque([root])

        response = 0

        while q:
            node = q.pop()

            if low <= node.val <= high:
                response += node.val

            if node.val >= low and node.left:
                q.appendleft(node.left)

            if node.val <= high and node.right:
                q.appendleft(node.right)

        return response
