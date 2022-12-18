from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        levelOrder = []
        q = deque([root])

        while q:
            newQ = deque()
            level = []

            while q:
                node = q.pop()

                level.append(node.val)

                if node.left:
                    newQ.appendleft(node.left)

                if node.right:
                    newQ.appendleft(node.right)


            q = newQ
            levelOrder.append(level)

        resp = []

        for level in levelOrder:
            resp.append(level[-1])

        return resp
