'''
Given the root of a binary tree, determine if it is a valid bst.


A valid bst:
- Left subtree contains only nodes with keys < nodes key
- Right subtree contains only ndoes with keys > nodes key
- Both the left and right subtrees must also be binary search trees

Ok so have a conditional statement that we update as we traverse.
- Evaluate if the statement holds
- Update statement for next iteration
- If it ever fails, return false
- Else return true

'''

from collections import deque

class Solution:
    def isValidBST(self, root):
        q = deque([(float('-inf'), root, float('inf'))])

        while q:
            l, node, r = q.pop()

            if not (l < node.val < r):
                return False

            if node.left:
                q.appendleft((l, node.left, node.val))

            if node.right:
                q.appendleft((node.val, node.right, r))

        return True
