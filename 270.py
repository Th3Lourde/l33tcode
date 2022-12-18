class Solution:
    def closestValue(self, root, target):
        self.ans = float('-inf')

        def dfs(node, target):
            if not node:
                return

            if abs(target - node.val) < abs(target - self.ans):
                self.ans = node.val

            if node.val >= target and node.left:
                dfs(node.left, target)

            if node.val <= target and node.right:
                dfs(node.right, target)

        dfs(root, target)

        return self.ans

'''
    1       <
   N  2

3.42

dfs(1, 3.5)

'''
