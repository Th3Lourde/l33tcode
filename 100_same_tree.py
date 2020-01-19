
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        if p == None and p == q:
            return True

        elif p != None and q != None:
            if p.val == q.val:
                r1 = self.isSameTree(p.left, q.left)
                r2 = self.isSameTree(p.right, q.right)

                if r1 == True and r1 == r2:
                    return True
                else:
                    return False

            elif p.val != q.val:
                return False

        else:
            return False


if __name__ == '__main__':
    '''
        1        1
       / \      / \
      2   3    2   3
    '''

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)



    q = TreeNode(1)
    q.left = TreeNode(2)
    # q.right = TreeNode(3)

    s = Solution()

    print(s.isSameTree(p,q))
