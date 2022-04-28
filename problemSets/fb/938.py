'''
Range sum BST

Given the root of a binary search tree and two integers,
return the sum of all values of nodes where the values is
in [lo, hi]

bfs, if node value is within range, add to sum
'''

from collections import deque

class Solution:
    def rangeSumBST(self, root, low, high):
        rangeSum = 0
        q = deque([root])

        while q:
            node = q.pop()

            if low <= node.val <= high:
                rangeSum += node.val

            if node.left:
                q.appendleft(node.left)

            if node.right:
                q.appendleft(node.right)

        return rangeSum
