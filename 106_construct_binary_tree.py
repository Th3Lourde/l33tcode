'''
last element of post is root

    3
   / \
  9   20
 /   /  \
1   15   7

in:   [1,9,3,15,20,7]
post: [1,9,15,7,20,3]

i for inOrder
p for postOrder

while in[i] == post[p]:
    # create node,



    3
   / \
  9   20

in: [9,3,20]
post: [9,20,3]

    3
     \
      4
       \
        5

in: [3,4,5]
post: [5,4,3]

If we have been creating nodes, in[i] != post[p] means we have hit the 'root'.
If we have not been creating node, in[i] != post[p] means we are performing a right run.
'''

'''
    3
   / \
  9   20
 /   /  \
1   15   7

build: None
roots = {3: 3 | .left = 9 | .left = 1}
roots = {3: 3 | .left = 9 | .left = 1, 20: 20 | .left 15}

in:   [1,9,3,15,20,7] | i = 5
post: [1,9,15,7,20,3] | p = 4

node = 20 7
tmp =  None

# Solution from the internet.
# My solution was very messy. Better use of time to find the cleaner solution.
# Come back to this later and try to derive/understand it.
class Solution:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        def recur(low, high):
            if low > high: return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)





'''







class Solution:
    def buildTree(self, inorder, postorder):
        build = None # true = left, false = right
        node = None
        roots = {}

        i = 0
        p = 0

        while i != len(inorder) or p != len(postorder):
            if inorder[i] == postorder[p]:
                # Build left
                # have left vs. right?

                if node:
                    if build:
                        tmp = TreeNode(inorder[i], node, None)
                        node = tmp
                        i += 1
                        p += 1

                    else:
                        return TreeNode(postorder[p], None, node)

                elif not node:
                    node = TreeNode(inorder[i])
                    build = True
                    i += 1
                    p += 1

            elif inorder[i] != postorder[p]:
                # If node: have found local root

                if node:
                    if build:
                        tmp = TreeNode(inorder[i], node, None)
                        roots[inorder[i]] = tmp
                        node = None
                        tmp = None
                        build = None

                        i += 1

                    else:
                        tmp = TreeNode(postorder[p], None, node)
                        node = tmp

                        p += 1

                elif not node:
                    build = False
                    node = TreeNode(postorder[p])

                    p += 1
