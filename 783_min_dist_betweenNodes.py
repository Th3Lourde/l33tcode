'''
So perform a dfs, only pass ans.
everytime you see a new node, calculate
the difference between the values.

ans = min(ans, diff)

Ok so it's the difference between any nodes.

Get all of the values of the nodes, put them
into a list, sort the list, iter through list,
looking through the smallest diff

Or: For each node, look for the largest node
smaller or the smallest node larger. Compute diff.

Let's do both.

'''

class Solution:

    def minDiffInBST(self, root):
        ans = [float('inf')]

        def getLargest(val, node):
            while node != None:
                tmp = node.val
                node = node.right
            return abs(val-tmp)

        def getSmallest(val, node):
            while node != None:
                tmp = node.val
                node = node.left
            return abs(val-tmp)

        def dfs(node, ans):
            # Get answer for this node
            diff1, diff2 = float('inf'), float('inf')

            if node.left:
                diff1 = getLargest(node.val, node.left)
                dfs(node.left, ans)

            if node.right:
                diff2 = getSmallest(node.val, node.right)
                dfs(node.right, ans)

            ans[0] = min(ans[0], min(diff1, diff2))

        dfs(root, ans)

        return ans[0]

    def minDiffInBST_I(self, root):
        nodes = []

        def dfs(node, nodes):
            nodes.append(node.val)

            if node.left != None:
                dfs(node.left, nodes)

            if node.right != None:
                dfs(node.right, nodes)

        dfs(root, nodes)

        nodes.sort()

        ans = float('inf')

        for i in range(len(nodes)-1):
            ans = min(ans, nodes[i+1]-nodes[i])

        return ans
