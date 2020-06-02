'''
Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

So we will be given a node, which represents the root of the
binary search tree, and we want to support the pieces of
functionality:
1) return the next smallest number
2) return whether or not we have a next smallest number

This is a heap problem?

.next() .hasNext() both run 0(1). This is sounding more
like a heap problem. Iterate through the elements of the tree.
Create a min heap.

We can also just iterate through the tree via preOrder
and use that as our data structure. Let's do that.

What doesn't fit is that we use 0(n) for memory and not 0(h).

We want inOrder, not preOrder

["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):

        self.inOrder = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if type(node) == type(1):
                    self.inOrder.append(node)

                else:
                    stack.append(node.right)
                    stack.append(node.val)
                    stack.append(node.left)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        ans = self.inOrder[0]
        del self.inOrder[0]
        return ans


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.inOrder) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
