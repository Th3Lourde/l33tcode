class Solution:
    def zigzagLevelOrder(self, root):

        levelOrder = []


        def dfs(node, level):
            if not node:
                return

            if level >= len(levelOrder):
                levelOrder.append([node.val])
            else:
                levelOrder[level].append(node.val)

            if node.left:
                dfs(node.left, level+1)

            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)

        for i in range(len(levelOrder)):
            if i % 2 == 1:
                levelOrder[i] = levelOrder[i][::-1]

        return levelOrder
