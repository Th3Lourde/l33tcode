'''
So we care about logging
the leaf nodes in a l → r
manner and return the values
in a list.

So do dfs. If we get a leaf-node,
append it to a stack.

Do same for both r1, r2.

Return whether or not the two lists
are the same.

'''

class Solution:
    def leafSimilar(self, root1, root2):
        stack = [root1]
        node = root1
        leaf1 = []

        while stack:
            node = stack.pop()

            if node:
                if not node.left and not node.right:
                    # We are at a leaf-node
                    leaf1.append(node.val)

                else:
                    stack.append(node.left)
                    stack.append(node.right)

        stack = [root2]
        node = root2
        leaf2 = []

        while stack:
            node = stack.pop()

            if node:
                if not node.left and not node.right:
                    # We are at a leaf-node
                    leaf2.append(node.val)

                else:
                    stack.append(node.left)
                    stack.append(node.right)

        return leaf1 == leaf2
