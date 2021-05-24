
from collections import deque
class Solution:
    def levelOrder(self, root):
        levelOrder = []
        tmpLevel = []

        tmpQ = deque()
        q = deque()

        if root:
            q.append(root)

        while q:
            node = q.popleft()
            tmpLevel.append(node.val)

            if node.left:
                tmpQ.append(node.left)

            if node.right:
                tmpQ.append(node.right)

            if not q:
                q = tmpQ
                tmpQ = deque()

                if len(tmpLevel) > 0:
                    levelOrder.append(tmpLevel)
                    tmpLevel = []

        return levelOrder
