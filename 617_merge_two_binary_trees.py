class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{}".format(self.val)

class Solution:
    def mergeTrees(self, t1, t2):

        def merge(t1, t2):
            t1.val += t2.val

            if t2.left and not t1.left:
                t1.left = t2.left
            elif t1.left and t2.left:
                merge(t1.left, t2.left)

            if t2.right and not t1.right:
                t1.right = t2.right
            elif t1.right and t2.right:
                merge(t1.right, t2.right)

        if t1 and t2:
            merge(t1,t2)
            return t1
        elif t1:
            return t1
        elif t2:
            return t2


if __name__ == '__main__':
    '''
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
    '''

    one = TreeNode(1)
    three = TreeNode(3)
    two = TreeNode(2)
    five = TreeNode(5)

    one.left = three
    three.left = five

    one.right = two



    two = TreeNode(2)
    one_1 = TreeNode(1)
    four = TreeNode(4)
    three_1 = TreeNode(3)
    seven = TreeNode(7)

    two.left = one_1
    one_1.right = four
    two.right = three_1
    three_1.right = seven

    s = Solution()
    s.mergeTrees(one, two)
