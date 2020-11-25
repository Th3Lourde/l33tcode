
'''
If we do in-order, we get the nodes in an order
that is useful to us.

We can create a list out of this.

We can then use a two-pointer approach to create
our third list, which we return.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1, root2):
        self.myList = []

        def inOrder(node):
            if node == None:
                return

            inOrder(node.left)
            self.myList.append(node.val)
            inOrder(node.right)

        inOrder(root1)
        a = list(self.myList)

        self.myList = []

        inOrder(root2)
        b = list(self.myList)

        ans = []

        ida = idb = 0

        if len(a) == 0:
            ida = -1

        if len(b) == 0:
            idb = -1

        while ida >= 0 and idb >= 0:
            if a[ida] < b[idb]:
                ans.append(a[ida])
                ida += 1
                if ida > len(a)-1: ida = -1
            else:
                ans.append(b[idb])
                idb += 1
                if idb > len(b)-1: idb = -1

        if ida >= 0:
            ans += a[ida:]

        if idb >= 0:
            ans += b[idb:]

        self.myList = []
        return ans

def configureTrees():
    r1 = TreeNode(2)
    r1.left = TreeNode(1)
    r1.right = TreeNode(4)

    r2 = TreeNode(1)
    r2.left = TreeNode(0)
    r2.right = TreeNode(3)

    return r1, r2

def configureTreesII():
    r1 = TreeNode(0)
    r1.left = TreeNode(-10)
    r1.right = TreeNode(10)

    r2 = TreeNode(5)
    r2.left = TreeNode(1)
    r2.right = TreeNode(7)
    r2.left.left = TreeNode(0)
    r2.left.right = TreeNode(2)

    return r1, r2


if __name__ == '__main__':
    r1, r2 = configureTreesII()

    s = Solution()

    print(s.getAllElements(r1, r2))
