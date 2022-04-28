from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root: return []

        level_order = []
        q = deque([root])

        while q:
            new_q = deque()
            level = []

            while q:
                node = q.pop()

                level.append(node.val)

                if node.left:
                    new_q.appendleft(node.left)

                if node.right:
                    new_q.appendleft(node.right)

            if len(level) > 0:
                level_order.append(level)

            q = new_q

        resp = []

        for level in level_order:
            resp.append(level[-1])

        return resp
