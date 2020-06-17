"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
So preorder.

do we just loop through the children in reversed order
and append them to our stack?

do dfs only use what is mentioned above when pushing to stack
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        pre = []

        while stack:
            node = stack.pop()

            if node:
                pre.append(node.val)

                for child in reversed(node.children):
                    stack.append(child)

        return pre
