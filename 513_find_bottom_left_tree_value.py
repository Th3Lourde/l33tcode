'''
Given a binary tree,
find the leftmost value in the last row
of the tree.

So it's the left-most value whenever we see the
level for the first time.

So standard level-order traversal, only store
the node-value whenever we see a level for the
first time.

'''

class Solution:
    def findBottomLeftValue(self, root):

        ans = 0
        lvl = -1

        q = [ [0, root] ]

        while q:
            node = q.pop()

            if node[0] > lvl:
                ans = node[1].val
                lvl = node[0]

            if node[1].left:
                q.insert(0, [node[0]+1, node[1].left])

            if node[1].right:
                q.insert(0, [node[0]+1, node[1].right])

        return ans
