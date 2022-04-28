
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root):
        leafSum = 0

        q = deque([(root, False)])

        while q:
            node, left = q.pop()

            if left == True and node.left == None and node.right == None:
                leafSum += node.val

            if node.left:
                q.appendleft((node.left, True))

            if node.right:
                q.appendleft((node.right, False))

        return leafSum
