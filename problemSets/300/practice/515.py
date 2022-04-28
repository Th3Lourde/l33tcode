'''
Given the root of a binary tree
return an array of the largest value in each row

level order, max

bfs, have an level, node for each value.
Have an array where arr[i] is the max of row i.

'''

from collections import deque

class Solution:
    def largestValues(self, root):
        q = deque([[0, root]])
        ans = []

        if not root:
            return ans

        while q:
            level, node = q.pop()

            if level >= len(ans):
                ans.append(node.val)
            else:
                ans[level] = max(ans[level], node.val)

            if node.left:
                q.appendleft([level+1, node.left])

            if node.right:
                q.appendleft([level+1, node.right])

        return ans
