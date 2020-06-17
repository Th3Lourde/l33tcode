"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
Just store the value as well as the node
If not node[0], ans = max(ans, ans[1])
'''

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        ans = 0

        stack = [ [root, 1] ]

        while stack:
            node = stack.pop()

            if node[0]:
                for c in reversed(node[0].children):
                    stack.append([c, node[1]+1])

                ans = max(ans, node[1])


        return ans
