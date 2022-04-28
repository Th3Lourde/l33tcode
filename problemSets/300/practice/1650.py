"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

'''
dfs to the node
make the larger path a set
the smaller one a list
'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()

        while True:
            if p:
                if p.val in seen:
                    return p

                seen.add(p.val)
                p = p.parent

            if q:
                if q.val in seen:
                    return q

                seen.add(q.val)
                q = q.parent
