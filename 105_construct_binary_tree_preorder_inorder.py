'''
Test cases:
[3,9,20,15,7] <--- preorder
[9,3,15,20,7] <--- inorder

[1,2,4,5,3,6,7]
[4,2,5,1,6,3,7]

[1,2,4,5]
[4,2,5,1]

[1,3,6,7]
[1,6,3,7]

        3
     9    20
        15  7

pre = [3,9,20,15,7]
in  = [9,3,15,20,7]

p = []
i = [2, 5, 1, 6, 3]

build(None)
    p.pop(1)
    r = TreeNode(1)
    r.left = build(1)
        build(1)
        p.pop(2)
        r = TreeNode(2)
        r.left = build(2)
            build(2)
            p.pop(4)
            r = TreeNode(4)
            r.left = build(4)
                build(4)
                p.pop(5)
                r = TreeNode(5)
                r.left = build(5)
                    build(5)
                    p.pop(3)
                    r = TreeNode(3)
                    r.left = build(6)
                    i.pop(4)
'''

class Solution:
    def buildTree(self, preorder, inorder):
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()

        return build(None)
