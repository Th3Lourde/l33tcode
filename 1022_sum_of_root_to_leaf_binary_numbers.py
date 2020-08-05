'''
Ok so what's the goal?

Ok so we are given a tree, each node in the tree
either has a value of one or zero.

Each root to leaf path represents a binary number

return the sum of all of the binary numbers

Ok so let's use dfs.

Let's store two values in every element in our stack.

The first value is the node, the second value is the
current binary number that we have.

We can initially represent this binary number as a string,
everytime we see a new node, add the value of the node to
the rhs of the string.

This will require us to check if the node that we are at
if a leaf node.




'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        ans = 0

        stack = [[root, ""]]

        while stack:
            node = stack.pop()

            if node[0] != None:
                bin = node[1] + str(node[0].val)

                if node[0].left == None and node[0].right == None:
                    ans += int(bin, 2)

                else:
                    stack.append([node[0].left, bin])
                    stack.append([node[0].right, bin])

        return ans
