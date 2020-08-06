'''
Given a tree, and a value,
insert a value into the tree.

Start at a node.

We are given that the value we have
been given does not currently exist
in our tree.

If the node.val > our val:
    go left

elif node.val < our val:
    go right

Traverse until the .left
or the .right doesn't exist,
then add the value to the tree.




'''

class Solution:
    def insertIntoBST(self, root, val):

        if not root:
            return TreeNode(val)

        node = root

        while True:
            if node.val > val:

                # Go left
                if node.left == None:
                    node.left = TreeNode(val)
                    return root

                node = node.left

            elif node.val < val:

                # Go right
                if node.right == None:
                    node.right = TreeNode(val)
                    return root

                node = node.right
