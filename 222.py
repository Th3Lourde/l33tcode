from collections import deque

class Solution:
    def countNodes(self, root):
        count = 0

        if not root:
            return count

        def getHeight(node, height):
            if not node:
                return height

            return getHeight(node.left, height+1)

        height = getHeight(root, 0)

        # print(height)

        if height == 1:
            count += 1

            if root.left:
                count += 1

            if root.right:
                count += 1

            return count

        depth = 1

        q = deque([root])

        while depth < height-1:
            newQ = deque()

            while q:
                node = q.pop()

                if node.right:
                    newQ.appendleft(node.right)

                if node.left:
                    newQ.appendleft(node.left)

            q = newQ
            depth += 1

        # print(q)

        while q:
            # print("foo")
            node = q.pop()

            if node.left:
                count += 1

            if node.right:
                count += 1

            if node.right or node.left:
                # print("len q: {}".format(len(q)))
                count += 2*len(q)
                break

        # print("Count of last level = {}".format(count))

        for i in range(0, height-1):
            count += 2**i

        return count
