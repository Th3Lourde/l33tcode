'''
Given a binary tree, and two nodes
in the tree, find the lowest common
ancestor of the two nodes.

dfs to find both nodes,
start from end and work backwards.

Construct a set to answer the question of:
"Is this node in the other path?"

'''


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        def dfs(root, targ):
            stack = [ [root, [] ] ]

            while stack:
                node = stack.pop()

                if node[0].val == targ:
                    node[1].append(node[0].val)
                    return node[0], node[1]

                if node[0].left:
                    stack.append([node[0].left, list(node[1]+[node[0].val])])

                if node[0].right:
                    stack.append([node[0].right, list(node[1]+[node[0].val])])

        # 1) Find p
        _, p_path = dfs(root, p.val)

        # 2) Find q
        _, q_path = dfs(root, q.val)

        while True:
            p_n = p_path.pop()

            if p_n in q_path:
                ans, _ = dfs(root, p_n)
                return ans

            q_n = q_path.pop()

            if q_n in p_path:
                ans, _ = dfs(root, q_n)
                return ans
