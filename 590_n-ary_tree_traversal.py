"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
Same thing, only change when you log the value
'''

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        postOrd = []

        while stack:
            node = stack.pop()

            if node or node == 0:
                if type(node) == type(1):
                    postOrd.append(node)

                else:
                    stack.append(node.val)
                    for c in reversed(node.children):
                        stack.append(c)

        return postOrd
