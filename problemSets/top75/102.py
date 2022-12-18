'''
Given the root of a binary tree, return the level order
traversal of its nodes' values

Soooooooo bfs.
put each 'iteration' in a queue,
for each level, drain the queue, then add the nodes
for the next level,
repeat until out of levels

'''


from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        levelOrder = []

        while q:
            newQ = deque([])
            currentLevel = []

            while q:
                node = q.pop()

                currentLevel.append(node.val)

                if node.left:
                    newQ.appendleft(node.left)

                if node.right:
                    newQ.appendleft(node.right)

            if len(currentLevel) > 0:
                levelOrder.append(currentLevel)

            q = newQ

        return levelOrder
