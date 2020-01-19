
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
in:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

     4
   /   \
  7     2
 / \   / \
6   9 1   3
'''

'''
out:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

'''
starting point is node
cmpy node.left
node.left = node.right
node.right = tmp
continue down node.left, node.right, until
there is nothing left
'''



class Solution:
    def invertTree(self, root):
        def iter(node):
            if node:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                iter(node.left)
                iter(node.right)

        iter(root)
        return root
