'''
Given the root of a BST,
convert it to a Greater Tree.

A Greater Tree is a tree ∋ you
add the values of all nodes that
have a greater val than the given
node.

Traverse through the largest elements.

traverse(node, sum):

    s = sum

    if node.right:
        s = traverse(node.right, s)

    node.val += s

    if node.left:
        s = traverse(node.left, s)

    return max(node.val, s)

Solution 1:
    - Get all nodes in the tree, for each
    node, figure out what the actual val
    should be.

    Do another iteration, update the vals.


traverse(4, 0)
    s = 26
    node.val += 26 =  30

    traverse(node.left):
        traverse(1, 30):
            traverse(2, 30):
                traverse(3, 30):
                    node.val += 30
                    return 33

                node.val += 33
                return 35

            node.val += 35 ⟹ 36

            traverse(0, 36):
                return 36






traverse(6, 0)
    s = 15
    node.val = 6 + 15 = 21

    traverse(5, 21)
        s = 21
        return 26

    return max(21, 26) ⟹ 26


traverse(7, 0):
    s = 8
    node.val = 7 + 8 = 15
    node.left = None
    return 15

traverse(8, 0):
    node.right = None
    node.val = 8
    node.left = None
    return 8



'''

class Solution:
    def bstToGst(self, root):

        def traverse(node, sum):
            s = sum

            if node.right:
                s = traverse(node.right, s)

            node.val += s

            if node.left:
                s = traverse(node.left, s)

            return max(node.val, s)


        traverse(root, 0)

        return root
