'''
Given the root of a binary tree, check whether
it is a mirror  of itself (symmetric around the center)

Get the level order of the tree (including nones)

go through each level, check if the level is a palindrome.

return if all levels are a palindrome

0(n)
0(n)
'''


class Solution:
    def isSymmetric(self, root):
        levels = []

        def dfs(node, level):
            if not node:
                if level >= len(levels):
                    levels.append(["None"])
                else:
                    levels[level].append("None")

                return

            if level >= len(levels):
                levels.append([node.val])
            else:
                levels[level].append(node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)

        for level in levels:
            l = 0
            r = len(level)-1

            while l < r:
                if level[l] != level[r]:
                    return False

                l += 1
                r -= 1

        return True
