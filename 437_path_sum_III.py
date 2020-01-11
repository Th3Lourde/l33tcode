
'''
Write out the iterative/recursive solution
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Iterative
    def pathSum(self, root, sum):

        def path_itr(node, path, target):
            path = 0
            while True:
                if node:
                    if node != l2[-1][0]:
                        # Go left
                        path += node.val
                        l2.append([node,path])

                        if path == target:
                            ans[0] += 1

                        node = node.left

                    elif node == l2[-1][0]:
                        # Go right
                        tmp = l2.pop()
                        path = tmp[-1]

                        node = node.right

                elif not node:
                    if l2 == [['h','h']]:
                        break

                    elif l2 != [['h','h']]:
                        node = l2[-1][0]



        def itr_itr(node): # move through the bt, call path_itr on every node
            while True:
                if node:

                    if l1[-1] == node:
                        # go right
                        l1.pop()
                        node = node.right

                    elif l1[-1] != node:
                        # go left
                        path_itr(node, 0, sum) # Find all possible paths
                        l1.append(node)
                        node = node.left

                if not node:
                    if l1 == ['h']:
                        break

                    elif l1 != ['h']:
                        node = l1[-1]




        ans = [0]
        # path = 0

        l1 = ['h'] # for finding all of the proper starting places
        l2 = [['h','h']] # for finding all of the paths of a certain starting place
        itr_itr(root)

        return ans[0]


    # Recursive
    def pathSum_r(self, root, sum): # sum is really target
        def itr_path(node, path, target):
            if node:
                path += node.val

                if path == target:
                    ans[0] += 1

                itr_path(node.left, path, target)
                itr_path(node.right, path, target)

        def itr_rec(node):
            if node:
                itr_path(node, 0, sum)
                itr_rec(node.left)
                itr_rec(node.right)


        ans = [0]
        path = 0
        itr_rec(root)

        return ans[0]


if __name__ == '__main__':
    s = Solution()


    '''
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
    '''

    root = TreeNode(10)
    a = TreeNode(5)
    b = TreeNode(-3)

    root.left = a
    root.right = b

    c = TreeNode(3)
    d = TreeNode(2)
    e = TreeNode(11)

    a.left = c
    a.right = d

    b.right = e


    f = TreeNode(3)
    g = TreeNode(-2)
    c.left = f
    c.right = g

    h = TreeNode(1)
    d.right = h


    print(s.pathSum(root, 8))
