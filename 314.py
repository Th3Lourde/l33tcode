'''
Have a global list where the index of the list
represents the vertical order of the node.

Perform traversals in a dfs manner, pre-order
traversal to ensure that the nodes at same

maybe we should go left as much as we can
in order to determine what the level should
initialize things at

Or, start at zero and save the min key
and start from the min key when creating
the list

'''

from collections import deque

class Solution:
    def verticalOrder(self, root):
        vOrder = {}
        self.minLevel = float('inf')
        ans = []

        # def dfs(node, level):
        #     if not node:
        #         return
        #
        #     self.minLevel = min(self.minLevel, level)
        #
        #     if level in vOrder:
        #         vOrder[level].append(node.val)
        #     else:
        #         vOrder[level] = [node.val]
        #
        #     if node.left:
        #         dfs(node.left, level-1)
        #
        #     if node.right:
        #         dfs(node.right, level+1)
        #
        # dfs(root, 0)

        if not root:
            return []

        q = deque([(root,0)])

        while len(q) > 0:
            node, level = q.pop()

            self.minLevel = min(self.minLevel, level)

            if level in vOrder:
                vOrder[level].append(node.val)
            else:
                vOrder[level] = [node.val]

            if node.left:
                q.appendleft((node.left, level-1))

            if node.right:
                q.appendleft((node.right, level+1))

        while self.minLevel in vOrder:
            ans.append(vOrder[self.minLevel])
            self.minLevel += 1

        print(vOrder)

        return ans
