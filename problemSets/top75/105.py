class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            inOrderIdx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[inOrderIdx])
            root.left = self.buildTree(preorder, inorder[0:inOrderIdx])
            root.right = self.buildTree(preorder, inorder[inOrderIdx+1:])
            return root
