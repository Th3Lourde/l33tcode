
'''
Given a binary tree, determine if it is balanced
A balanced binary tree is defined as a binary tree
in which the left and right subtrees of every node
differ in height by no more than 1


Approach A):
1) Write a function that finds the height of a binary
tree
2) Find the height of the left, right subtree
3) If difference in height > 1, return False
    - else return True

Iterate through the tree via recursion, then stack (iterative)
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # is faster
    class Solution:
        def isBalanced(self, root: TreeNode) -> bool:
            return self.height(root) != -1

        def height(self, root):
            if not root:
                return 0
            lHeight = self.height(root.left)
            rHeight = self.height(root.right)
            if lHeight == -1 or rHeight == -1 or abs(lHeight - rHeight) > 1:
                return -1
            return max(lHeight, rHeight) + 1

class Solution:





    # Didn't finish, hassle
    def isBalanced(self, root):
        def getHeight(node, stack, maxH):
            while True:
                if node:
                    if node != stack[-1]:
                        maxH

                    elif node == stack[-1]:
                        ...


                    ...
                elif not node:



                    ...




            # if node:
            #     maxH += 1
            #     h1 = getHeight(node.left, maxH)
            #     h2 = getHeight(node.right, maxH)
            #     return max(h1,h2)
            #
            # elif not node:
            #     return maxH

        def itr(node, stack):
            while True:
                if node:
                    if abs(getHeight(node.left, ["h"], 0) - getHeight(node.right, ["h"], 0)) > 1:
                        return False

                    if node != stack[-1]:
                        # go left
                        stack.append(node)
                        node = node.left

                    elif node == stack[-1]:
                        # go right
                        stack.pop()
                        node = node.right

                    # r1 = itr(node.left)
                    # r2 = itr(node.right)

                    # if r1 and r2:
                    #     return True

                elif not node:
                    if stack == ["h"]:
                        return True

                    elif stack != ["h"]:
                        node = stack[-1]


        if root == None:
            return True

        if itr(root, ["h"]):
            return True

        return False




if __name__ == '__main__':
    s = Solution()


    '''
        3
       / \
      9  20
        /  \
       15   7
    '''

    root = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    root.left = a
    root.right = b

    c = TreeNode(15)
    d = TreeNode(7)
    b.left = c
    b.right = d

    print(s.isBalanced(root))


    '''
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
    '''

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(2)
    root.left = a
    root.right = b

    c = TreeNode(3)
    d = TreeNode(3)
    a.left = c
    a.right = d

    e = TreeNode(4)
    f = TreeNode(4)
    c.left = e
    c.right = f

    print(s.isBalanced(root))
