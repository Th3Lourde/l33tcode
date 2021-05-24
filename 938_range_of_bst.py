class Solution:
    def rangeSumBST(self, root, low, high):
        ans = [0]

        def dfs(node, ans):
            if low <= node.val <= high:
                ans[0] += node.val

            if node.val != low and node.left:
                dfs(node.left, ans)

            if node.val != high and node.right:
                dfs(node.right, ans)

        dfs(root, ans)

        return ans[0]
