'''
Given the roots of binary trees p and q, write a function
to check if the trees are the same or not

Just do a dfs with both nodes, with check that everything is the same
'''

class Solution:
    def isSameTree(self, p, q):
        def dfs(nodeA, nodeB):
            if nodeA and nodeB and nodeA.val == nodeB.val:
                return dfs(nodeA.left, nodeB.left) and dfs(nodeA.right, nodeB.right)

            elif not nodeA and not nodeB:
                return True

            else:
                return False

        return dfs(p, q)
