


class Solution:

    def isSubPath(self, head, root):

        def dfs(root, targ):
            ans = []

            if not root:
                return ans

            if root.val == targ:
                ans.append(root)

            if root.left:
                node = root.left
                stack = ["L", root]

            elif root.right:
                node = root.right
                stack = ["L"] # Is this a problem?

            else:
                return

            while stack != []:
                if node:

                    if node == stack[-1]:
                        stack.pop()
                        node = node.right

                    elif node != stack[-1]:

                        if node.val == targ:
                            ans.append(node)

                        stack.append(node)
                        node = node.left

                if not node:

                    if stack == ["L"]:
                        return ans

                    elif stack != ["L"]:
                        node = stack[-1]

        hits = dfs(root, head.val)

        queue = []

        if len(hits) != 0 and head.next == None:
            return True

        for hit in hits:

            if hit.left:
                if hit.left.val == head.next.val:

                    queue.append([hit.left, head.next])

            if hit.right:
                if hit.right.val == head.next.val:
                    queue.append([hit.right, head.next])

        while queue != []:
            term = queue.pop()

            if term[1].next == None:
                return True

            if term[0].left:
                if term[0].left.val == term[1].next.val:
                    queue.append([term[0].left, term[1].next])

            if term[0].right:
                if term[0].right.val == term[1].next.val:
                    queue.append([term[0].right, term[1].next])

        return False
