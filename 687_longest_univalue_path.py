'''
Given the root of a binary tree,
return the length of the longest path,
where each node in the path has the same value.

This path may or may not pass through the root.

dfs with the twist that we are adding a running sum
and a value to look out for

Ok so this doesn't cover instances where there is a left
and a right path.

So find the path below this node that has the max number
of similar nodes
'''

class Solution:
    def longestUnivaluePath(self, root):
        self.longest_run = 0

        def nodesValN(node, target, count):
            if not node or node.val != target:
                return count

            return max(nodesValN(node.left, target, count+1), nodesValN(node.right, target, count+1))


        def dfs(node):
            if not node:
                return

            self.longest_run = max(self.longest_run, nodesValN(node.left, node.val, 0)+nodesValN(node.right, node.val, 0))

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(root)

        return self.longest_run
