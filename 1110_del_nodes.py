
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root, to_delete):
        s = set()
        for n in to_delete:
            s.add(n)
        self.s = s

        self.ans = []
        self.traverseRoot(root)
        return self.ans

    def traverseRoot(self, root):
        if root == None:
            return
        elif root.val in self.s:
            self.traverseRoot(root.left)
            self.traverseRoot(root.right)
        else:
            self.ans.append(root)
            self.dfs(root)

    def dfs(self, node):
        # Base Case
        if node == None:
            return

            # Have found a deleted node
        if node.left != None:
            n = node.left
            if n.val in self.s:
                # Save children
                childL = n.left
                childR  = n.right

                # Delete node
                node.left = None

                # Traverse Children
                self.traverseRoot(childL)
                self.traverseRoot(childR)
        self.dfs(node.left)

            # Have found a deleted node
        if node.right != None:
            n = node.right
            if n.val in self.s:
                # Save children
                childL = n.left
                childR  = n.right

                # Delete node
                node.right = None

                # Traverse Children
                self.traverseRoot(childL)
                self.traverseRoot(childR)
        self.dfs(node.right)
