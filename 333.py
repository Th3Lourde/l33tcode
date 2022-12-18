'''
So we need to check to make sure that the
nodes are less than/greater than the parent nodes.

In order to do this, we should return min, max values,
which we can add on to the logic.

How do we initially populate left, right sides?
'''

class Solution:
    def largestBSTSubtree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, float('inf'), float('-inf')

            lcount, lmin, lmax = dfs(node.left)
            rcount, rmin, rmax = dfs(node.right)

            if lcount >= 0 and rcount >= 0 and node.val > lmax and node.val < rmin:
                count = 1 + lcount + rcount
                self.ans = max(self.ans, count)

                mmin = lmin if lcount else node.val
                mmax = rmax if rcount else node.val
                return count, mmin, mmax

            else:
                return -1, float('-inf'), float('inf')

        dfs(root)
        return self.ans
