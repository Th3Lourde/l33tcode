class Solution:
    def isValidBST(self, root):
        def validate(minVal, node, maxVal):
            if not node:
                return True

            if not minVal < node.val < maxVal:
                return False

            return validate(minVal, node.left, node.val) and validate(node.val, node.right, maxVal)

        return validate(float('-inf'), root, float('inf'))
