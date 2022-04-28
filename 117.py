from collections import deque

class Solution:
    def connect(self, root):
        levelOrder = []
        q = deque([root])

        while q:
            newQ = deque()
            nextLevel = []

            while q:
                node = q.pop()

                if not node:
                    continue

                nextLevel.append(node)
                newQ.appendleft(node.left)
                newQ.appendleft(node.right)

            q = newQ
            levelOrder.append(nextLevel)

        for level in levelOrder:
            for idx in range(len(level)-1):
                level[idx].next = level[idx+1]

        print(levelOrder)
        return root
