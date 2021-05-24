class Solution:
    def isSameTree(self, p, q):

        def nodesAreEqual(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False

            return n1.val == n2.val

        def dfs(nodeA, nodeB):
            if not nodesAreEqual(nodeA, nodeB):
                return False

            if not nodeA:
                return True

            return dfs(nodeA.left, nodeB.left) and dfs(nodeA.right, nodeB.right)

        return dfs(p, q)
