class Solution:
    def balanceBST(self, root):
        nodes = []

        def dfs(node, arr):

            if node.left:
                dfs(node.left, arr)

            arr.append(node.val)

            if node.right:
                dfs(node.right, arr)

        dfs(root, nodes)

        def build(l, r):
            if l > r:
                return

            m = (l+r)//2
            node = TreeNode(nodes[m])
            node.left = build(l, m-1)
            node.right = build(m+1, r)
            return node

        return build(0, len(nodes)-1)
