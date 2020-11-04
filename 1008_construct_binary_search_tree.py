'''
So we are given an array
of vals, which represent the
preorder traversal through a
BST.

We wish to return the root node
of the BST that the preorder
represents.

Going left:
use a stack to store what nodes
we have already seen

So the first node is the root.
As soon as we see a node > root,
now on rhs.

Proceed down the lhs of the tree, create
a stack as we go (also doing .left and creating nodes)

[8,5,1,7,10,12]
       ^

[8,5,1] (pop from right)
Also keep a hashMap that we can use to
perform a lookup of a node given a val

Populate RHS:

if current val < stack.peek():
    node.left()
    append node to dict
    append val to stack

if current val > stack.peek():
    # if stack = [root], go right
    # if < stack[-2], go right
    # if > stack[-2], pop

Populate LHS:

if val > stack.peek():
    go right

if val < stack.peek():
    go left


What if we have a left-bound, right bound
that we are working with?


We can also just read this level by level.

first node is first level
2-3 = second level
4-6 =

nodes = []
range = []

2*level

Initialize root.

nodes = 8, level = 2, idx = 1

new_nodes = []

for i in range(idx, idx+level, ):
    node = nodes.pop()

    if preorder[idx]:
        node.left = TreeNode(preorder[idx])
        new_nodes.append(node.left)

    if idx+1 == len(preorder):
        return

    if preorder[idx+1]:
        node.right = TreeNode(preorder[idx+1])
        new_nodes = [node.right] + new_nodes

    nodes = [node.left, node.right] + nodes



preorder = [8,5,1,7,10,12]
                  ^
root = Node(8)

nodes = [8]
level = 1
idx = 1
new_nodes = []

node = 8

pre[1]
8.left = 5
new_nodes = [5]
8.right = 10
new_nodes = [10, 5]

idx = 3
level = 2
top = 3 + 4 ⟹ 7
new_nodes = [10, 5]

node = 5
5.left = preorder[3]
nodes = [1, 10]

5.right = 7
nodes = [7, 1, 10]

idx += 2 ⟹ idx = 5

node = 10
preorder[5] == None, skip

Solved the wrong problem.

If we were given the post order, we'd
have done it correctly.

Have node
    look for first node < val, that's left (remove from list)
    look for first node < val, that's right (remove from list)

[8,5,1,7,10,12]

Do the first node first, store it as root.

[12]

nodes = [10, 5]

node = 5

5.left = 1
nodes = [1, 10]
5.right = 7
nodes = [7, 1, 10]

opts = [12]
node = 10

node.left = none
node.right = 12
done

pre = [5,1,7,10,12]

root = 8
nodes = [8]

node = 8

8.left = 5
nodes = [5]
pre = [1,7,10,12]

8.right = 10
nodes = [10, 5]
pre = [1,7,12]

node = 5

5.left = 1
nodes = [1, 10]
pre = [7,12]

5.right = 7
nodes = [7, 1, 10]
pre = [12]

node = 10

10.left = None

10.right = 12

preorder = []
nodes = [12, 7, 1, 10]

[10,3,19,14]
'''

class Solution:

    def bstFromPreorder(self, preorder):
        return self.buildTree(preorder[::-1], float('inf'))

    def buildTree(self, preorder, bound):
        if not preorder or preorder[-1] > bound: return None

        node = TreeNode(preorder.pop())
        print(node)
        node.left = self.buildTree(preorder, node.val)
        node.right = self.buildTree(preorder, bound)
        return node


    def bstFromPostOrder(self, preorder):
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])

        nodes = [root]
        level = 1
        idx = 1

        while idx < len(preorder):

            top = idx + (level * 2)

            while idx < len(preorder) and idx < top:
                node = nodes.pop()

                if preorder[idx]:
                    node.left = TreeNode(preorder[idx])
                    nodes = [node.left] + nodes

                if idx+1 == len(preorder):
                    return root

                if preorder[idx+1]:
                    node.right = TreeNode(preorder[idx+1])
                    nodes = [node.right] + nodes

                idx += 2

            level += 1

        return root
