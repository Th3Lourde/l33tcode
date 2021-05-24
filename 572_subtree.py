
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given the roots of two binary trees
return true if the tree subRoot exists
in root. Meaning that order is maintained
and that all of the values match and that there
aren't any values that have been added in one
tree vs. another

idea:

dfs. If the nodes match then check the .left and the .right.
Children of both must be None.

1) Find node in root that has same val as subRoot
2) Check if same.
'''

class Solution:
    def isSubtree(self, root, subRoot):

        def areTreesSame(n1, n2):
            if n1 == None and n2 == None:
                return True
            elif n1 == None or n2 == None:
                return False

            if n1.val != n2.val:
                return False

            return areTreesSame(n1.left, n2.left) and areTreesSame(n1.right, n2.right)

        def dfs(node):
            hasSubTree = False

            if node.val == subRoot.val:
                hasSubTree = areTreesSame(node, subRoot)

            if node.left and dfs(node.left):
                hasSubTree = True

            if node.right and dfs(node.right):
                hasSubTree = True

            return hasSubTree

        return dfs(root)
