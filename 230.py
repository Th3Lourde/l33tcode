class Solution:
    def kthSmallest(self, root, k):
        def inOrder(node, idx):
            if node.left:
                idx, ans = inOrder(node.left, idx)

                if idx == k:
                    return idx, ans

            idx += 1

            if idx == k:
                return idx, node.val

            if node.right:
                idx, ans = inOrder(node.right, idx)

                if idx == k:
                    return idx, ans

            return idx, None

        _, ans = inOrder(root, 0)

        return ans
