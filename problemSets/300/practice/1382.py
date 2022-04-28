
'''
Get all of the nodes, sort them
then start from the middle node and construct a tree

Given tree is a bst, so can just traverse to get the
nodes in sorted order (inOrder)


1) inOrder traversal to get the nodes in sorted order
2) create a new tree

0 1 2 3 4 5 6 7 8 9
1,2,3,4,5,6,7,8,9,10
    1     0   1


          6
       3     8
      2  4  7  9
     1  5       10

Keep a set of the values that we have seen before

given an index
create a node with the value of nodes[idx]
the node that goes on the left is mid between leftBound and idx
the node that goes on the right is mid between rightBound and idx

'''

creatTree(0, (0+9)//2, 9)

def mid(l,r):
    return (l+r)//2

     #        5
     #    2        8
     #  0   3    6   9
     #   1    4

mid(0,10)
    mid(0,4)
        mid(0,1)
            mid(1,1)
        mid(3,4)
            mid(4,4)
    mid(6,10)
        mid(6,7)
            mid(7,7)
        mid(9,10)
            mid(10,10)


class Solution:
    def balanceBST(self, root):
        nodesSorted = []

        def inOrder(node):
            if not node:
                return

            if node.left:
                inOrder(node.left)

            nodesSorted.append(node.val)

            if node.right:
                inOrder(node.right)


        inOrder(root)

        def createTree(l, r):
            if l > r:
                return

            m = (l+r)//2

            node = TreeNode(nodesSorted[m])
            node.left = createTree(l, m-1)
            node.right = createTree(m+1, r)

            return node

        return createTree(0, len(nodesSorted)-1)
