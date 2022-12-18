class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



'''
You need to construct a binary tree
from a string consisting of paren and integers

The whole input represents a binary tree. It contains
an integer followed by zero, one, or two pairs of parens

The integer represents the root's value and a pair of
parens contains a child binary tree with the same struct

Given this string, return the binary tree that this string
represents.

So we can traverse the list, create the left node, the right node,
and interate recursively until this is complete.

Another way to do this is to create the level order traversal of the
tree and then create the tree that way.

Let's explore the first option first.

0123456789012345 <-- idx
0112212210112210 <-- level
4(2(3)(1))(6(5))
         ^
dfs(4)
    dfs(2)
        dfs(3)


Call dfs on an index, dfs returns the idx that
we are left at after the dfs call.
- dfs on an index
- Create a tree node, the value of the node is the value at the index,
traverse right until you hit a paren or run out.
- Look for the next paren. If dne, return node


- figure out the 'root' value
- if the next paren is a "(", set that to be the treeNode.left, call dfs on the index after the "("
|--> start from the idx that this dfs returns if it is
- if the next paren is a ")", return that idx+1
- if the next paren is a "(", set that to be the treeNode.right, return the output of the dfs


'''

class Solution:
    def str2tree(self, s):
        def dfs(idx):
            # 1) Find the value of the root node
            isNeg = False
            node = TreeNode()
            val = []

            while idx < len(s) and s[idx] not in set({'(', ')'}):
                if s[idx] == '-':
                    isNeg = True
                else:
                    val.append(s[idx])

                idx += 1

            node.val = int("".join(val))

            if isNeg:
                node.val *= -1

            # 2) Find the value of the first child, if it exists
            # Next value can be:
            # - nothing |--> return
            # )         |--> return
            # (         |--> there is a left value, find it
            if idx >= len(s) or s[idx] == ")":
                return node, idx+1

            leftNode, idx = dfs(idx+1)
            node.left = leftNode

            # 3) Find the value of the second child, if it exists
            # Next value can be:
            # - Nothing |--> return
            # )         |--> return
            # (         |--> there is a left value
            if idx+1 >= len(s) or s[idx] == ")":
                return node, idx+1

            rightNode, idx = dfs(idx+1)
            node.right = rightNode

            return node, idx+1

        if len(s) == 0:
            return None

        root, _ = dfs(0)
        return root

'''
0123456789012345
4(2(3)(1))(6(5))
           ^

dfs(0):
    val = [4]
    node = Node(val=4)

    dfs(2):
        val = [2]
        node = Node(val=2)

        dfs(4):
            val = [3]
            node = Node(val=3)
            return Node(val=3), 6

        node = Node(val=2, left=Node(val=3))

        dfs(7):
            val = [1]
            node = Node(val=1)
            return Node(val=1), 9

        node = Node(val=2, left=Node(val=3), right=Node(val=1))
        idx = 10

    node = Node(val=4, left=Node(val=2, left=Node(val=3), right=Node(val=1)))
    idx = 10

    dfs(11):
        val = [6]
        node = Node(val=6)

        dfs






'''
