class Solution:
    def pathSum(self, root, targetSum):
        if not root: return None

        ans = []

        def dfs(node, path, pathSum):
            path.append(node.val)
            pathSum += node.val

            if node.left:
            # TODO: do this withouth creating a new path each time
                dfs(node.left, list(path), pathSum)

            if node.right:
                dfs(node.right, list(path), pathSum)

            if not node.left and not node.right:
                if pathSum == targetSum:
                    ans.append(list(path))

            path.pop()


        dfs(root, [], 0)
        return ans
