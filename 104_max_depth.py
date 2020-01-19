class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        r1 = self.iterate(root.left, 1)
        r2 = self.iterate(root.right, 1)

        if (r1 == None) and (r2 == None):
            return 1

        elif (r1 == None) and (r2 != None):
            return r2

        elif (r1 != None) and (r2 == None):
            return r1

        elif (r1 != None) and (r2 != None):
            return max(r1, r2)

    def iterate(self, root, max):
        if root == None:
            return None

        elif root != None:
            r1 = self.iterate(root.left, max+1)

            r2 = self.iterate(root.right, max+1)

            if r1 == None and r2 == None:
                return max+1

            elif r1 == None and r2 != None:
                return r2

            elif r1 != None and r2 == None:
                return r1

            elif r1 != None and r2 != None:
                if r1 > r2:
                    return r1
                elif r1 <= r2:
                    return r2


if __name__ == '__main__':
    '''
    Ex 1:

        3
       / \
      9  20
        /  \
       15   7
    '''

    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    # print(a)
    # print(b,c)
    # print(d,e)

    s = Solution()

    r = s.maxDepth(a)

    print(r)
