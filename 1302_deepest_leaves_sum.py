'''
Given a binary tree, return the sum
of values of its deepest leaves

1) Find the height of the tree
2) Sum the values of all nodes at such height.

1) bfs, level order traversal, create a dictionary
s.t. key = level, val = sum of nodes at that level

0: 1, 1: 2+3, 2: 4+5+6, 3: 7+8

Keep a local var that keeps track of level

return d[level]

0(n) run-time
0(n) = 0(n) memory complexity



'''

class Solution:
    def deepestLeavesSum(self, root): # This works, is slow

        d = {}
        q = [ [root, 0] ]

        h = 0

        while q:
            node = q.pop()

            if node[0]:
                h = max(h, node[1])

                # add val to dict
                try:
                    d[node[1]] += node[0].val

                except:
                    d[node[1]] = node[0].val

                # continue traversal
                q = [ [node[0].right, node[1]+1],  [node[0].left, node[1]+1]  ] + q


        return d[h]
