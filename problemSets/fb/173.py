class BSTIterator:
    def __init__(self, root):
        self.stack = []
        node = root

        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        x = node.right

        while x:
            self.stack.append(x)
            x = x.left

        return node.val

    def hasNext(self):
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
