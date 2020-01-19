

class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "TreeNode: 'val': {}, 'left': {}, 'right': {} ".format(self.val, self.left, self.right)

class Solution:

    def get_height(self, node: TreeNode, height=0) -> int:
    # def get_height(self, node: TreeNode, height=1) -> int:

        # print(node)

        if not(node):
            return height


        elif node.left != None and node.right != None:
            h1 = self.get_height(node.left, height+1)
            h2 = self.get_height(node.right, height+1)

            return max(h1,h2)

        elif node.left == None and node.right != None:
            h1 = self.get_height(node.right, height+1)
            return h1

        elif node.left != None and node.right == None:
            h1 = self.get_height(node.left, height+1)
            return h1

        elif node.left == None and node.right == None:
            return height


    def isBalanced(self, root: TreeNode) -> bool:
        '''
        For every node, calculate the height of
        the two children nodes. If the difference
        in the children nodes is not off by
        more than one, good. Else return false

        We will need to iterate through all nodes
        in the tree, and will also be getting heights
        of said nodes. We should probably make a
        function that will allow us to find the
        height of a node
        '''

        if not(root):
            return True

        elif root:
            h1 = self.get_height(root.left, 0)
            h2 = self.get_height(root.right, 0)

            print("h1: {} h2: {}".format(h1, h2))

            if abs(h1-h2) > 1:
                return False

            elif abs(h1-h2) <= 1:


                r1 = self.isBalanced(root.left)
                r2 = self.isBalanced(root.right)

                if r1 and r2:
                    return True

                else:
                    return False

if __name__ == '__main__':
    s = Solution()

    '''
    [1,2,2,3,3,null,null,4,4]

                1
            2       2
         3    3   n   n
       4   4

    '''

    r00t = TreeNode(1)
    a1 = TreeNode(2)
    a2 = TreeNode(2)
    b1 = TreeNode(3)
    b2 = TreeNode(3)
    c1 = TreeNode(4)
    c2 = TreeNode(4)

    r00t.left = a1
    r00t.right = a2

    a1.left = b1
    a1.right = b2

    b1.left = c1
    b1.right = c2

    t = Solution()

    '''
    Error Case 1:
    [1,null,2,null,3]
            1
      null    2
          null  3

    '''

    r00t = TreeNode(1)
    a1 = TreeNode(2)
    b1 = TreeNode(3)

    r00t.right = a1
    a1.right = b1

    # print(get_height(r00t, 0))
    # print(get_height(r00t.right, 0))

    # print(r00t)

    # print(t.isBalanced(r00t.left))
    # print(t.isBalanced(r00t.right))

    print(t.isBalanced(r00t))

    # print(t.get_height(r00t))
    # print(t.get_height(r00t.left))

    '''
    t.get_height(r00t.left) + 1 == t.get_height(r00t.right) + 1
    For all nodes, return yes, else return false
    '''



    # print(s.get_height(r00t.right.right))

    '''
    Analysis on what they mean by `every node`
        3
       / \
      9  20      This is ok
        /  \
       15   7

        3
       / \
      N  20      This is not ok. This only makes
        /  \     sense if you start counting at 3
       15   7




        3
       / \
      N  20      This is not ok.
        /  \
       N   7

         3
       /   \
      5    20
    /  \   /  \
   3    N  N   7


   Ok I don't really get why this is wrong. I don't think that I understand what they mean
   when they say `every node`. Come back to later and finish

    '''
