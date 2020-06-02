'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
'''

class Solution:
    def levelOrderBottom(self, root):

        if not root:
            return []

        stack = [[root, 0]]
        d = {}
        m = 0

        while stack:
            node = stack.pop()

            if node[0]:
                try:
                    d[node[1]].append(node[0].val)

                except:
                    d[node[1]] = [node[0].val]

                    # m = max(node[1], m)

                    m = node[1]


                stack.append(node[0].right)
                stack.append(node[0].left)

        ans = []

        for i in range(max, -1, -1):
            ans.append(d[i])

        return ans
