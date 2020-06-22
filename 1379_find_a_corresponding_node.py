'''
given two identical trees with different memory addresses.

given a node (target) in original.
find the node that target is a clone of in copy.

We are given that there do not exist any duplicates in the
tree, thus, we just perform a search in the cloned tree.

we will use dfs



'''

class Solution:
    def getTargetCopy(self, original, cloned, target): # Works
        targ = target.val
        stack = [cloned]

        while stack:
            node = stack.pop()

            if node:
                if node.val == targ:
                    return node

                stack.append(node.right)
                stack.append(node.left)

        return "ERROR"
