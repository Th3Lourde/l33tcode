class Solution:
    def zigzagLevelOrder(self, root):
        levels = []

        def levelOrder(level, node):
            if not node:
                return None

            if level >= len(levels):
                levels.append([node.val])
            else:
                levels[level].append(node.val)

            if node.left:
                levelOrder(level+1, node.left)

            if node.right:
                levelOrder(level+1, node.right)

        levelOrder(0, root)

        for idx in range(len(levels)):
            if idx % 2 == 1:
                levels[idx] = levels[idx][::-1]

        return levels
