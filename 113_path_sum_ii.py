
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

1) Traverse through the tree via dfs.
2) For every leaf whose path is the right value, perform a varied dfs search and return the path.
'''



class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []

        leafs = []

        stack = [[root, [], 0]]

        while stack:

            node = stack.pop()

            if node[0]:
                if not node[0].left and not node[0].right and node[2]+node[0].val == sum:
                    node[1].append(node[0].val)
                    tmp = list(node[1])
                    leafs.append(tmp)

                a = list(node[1])
                a.append(node[0].val)
                b = list(node[1])
                b.append(node[0].val)

                stack.append([node[0].right, a, node[2]+node[0].val])
                stack.append([node[0].left, b, node[2]+node[0].val])

        return leafs
