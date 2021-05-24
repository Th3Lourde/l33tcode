class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"

        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.data = data

        if self.data[0] == "N":
            return None

        node = TreeNode(self.data[:self.data.find(',')])
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])
        return node
