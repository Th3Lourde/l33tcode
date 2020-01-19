class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{}-->{}".format(self.val, self.right)

class Solution:
    # Given a binary tree, return the root
    # such that root.right.right.... will
    # yield a traversal such that you will
    # have gone in ascending order through
    # the nodes of the tree.

    def flatten(self, root, order):
        '''
        1. flatten left subtree
        2. find left subtree's tail
        3. set root's left to None, root's right to root'left, tail's right to root.right
        4. flatten the original right subtree
        '''

        if order == "pre-order":
            if not root:
                return

            self.prev = root
            self.flatten(root.left)

            tmp = root.right

            root.right, root.left = root.left, None

            self.prev.right = tmp

            # right = root.right

            # if root.left:
                # flatten root.left

            # flatten right subtree
            # self.flatten(right, "pre-order")
# if not root:
#         return
#     self.prev = root
#     self.flatten(root.left)
#
#     temp = root.right
#     root.right, root.left = root.left, None
#     self.prev.right = temp
#
#     self.flatten(temp)

            # # NLR
            # if root:
            #
            #     # now print the data of node
            #     print(root.val)
            #
            #     # First recur on left child
            #     self.flatten(root.left, order)
            #
            #
            #     # the recur on right child
            #     self.flatten(root.right, order)


        elif order == "in-order":
            # LNR
            if root:

                # First recur on left child
                self.flatten(root.left, order)

                # now print the data of node
                print(root.val)

                # the recur on right child
                self.flatten(root.right, order)


        elif order == "post-order":
            # LRN
            if root:

                # First recur on left child
                self.flatten(root.left, order)

                # the recur on right child
                self.flatten(root.right, order)

                # now print the data of node
                print(root.val)

if __name__ == '__main__':

    '''
         1
       /   \
      2     5
     / \   / \
    3   4 6   7
    '''

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)
    f = TreeNode(7)

    root.left = a
    root.right = d

    a.left = b
    a.right = c

    # d.left = e
    d.right = e

    # f = TreeNode("F")
    # b = TreeNode("B")
    # a = TreeNode("A")
    # d = TreeNode("D")
    # c = TreeNode("C")
    # e = TreeNode("E")
    # g = TreeNode("G")
    # i = TreeNode("I")
    # h = TreeNode("H")
    #
    # f.left = b
    # f.right = g
    #
    # b.left = a
    # b.right = d
    #
    # d.left = c
    # d.right = e
    #
    # g.right = i
    # i.left = h


    s = Solution()

    '''
    Depth-first traversal of an example tree:
        pre-order (red): F, B, A, D, C, E, G, I, H;
        in-order (yellow): A, B, C, D, E, F, G, H, I;
        post-order (green): A, C, E, D, B, H, I, G, F.
    '''
    root = s.flatten(root, "pre-order")
    # root = s.flatten(root, "post-order")
