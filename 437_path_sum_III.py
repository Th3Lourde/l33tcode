
'''
Write out the iterative/recursive solution
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:

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

'''
Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf,
but it must go downwards (i.e., traveling only from parent nodes to child nodes).

So this is just a normal tree, so there's no inherent order between the different nodes
in the tree.

We are given that the paths can only go downwards.

So get all paths, then start removing the top most node and see how
many of them end up hitting the target sum.

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

targetSum = 8

[10,5,3,3]  | 21 - 10 = 11
  r     l
[10,5,3,-2] | 16
[10,5,2,1]  | 18
[10,-3,11]  | 18

Do we need to check all of these?
I think so.

Could we just do this via recursive traversal
algo? Yes.

Each function call contains a list of sums.
Every time you hit a node, add the value of the node
to all of the sums. If any of the sums match the target
increment the global sum.
'''

class Solution:
    def pathSum(self, root, targetSum):
        self.hits = 0

        def findPaths(node, pathSums):
            if not node:
                return

            for idx in range(len(pathSums)):
                pathSums[idx] += node.val

                if pathSums[idx] == targetSum:
                    self.hits += 1

            if node.val == targetSum:
                self.hits += 1

            pathSums.append(node.val)

            findPaths(node.left, list(pathSums))
            findPaths(node.right, list(pathSums))


        findPaths(root, [])

        return self.hits


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
