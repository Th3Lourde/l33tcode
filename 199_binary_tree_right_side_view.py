'''
Given a binary tree, return
the values of the nodes you can see
ordered from top to bottom

Just traverse the tree. Every time
you see a node, append it to list and
go right.

Ok so I was wrong. Just do level order.
OverWrite (or write) the node value as
we traverse.

'''

class Solution:
    def rightSideView(self, root):
        if root == None:
            return []

        ans = []

        q = [ (root, 0) ]
        lvl = -1

        while q:
            node, level = q.pop()

            if level > lvl:
                lvl = level
                ans.append(node.val)

            else:
                ans[level] = node.val

            if node.left:
                q.insert(0, (node.left, level+1) )

            if node.right:
                q.insert(0, (node.right, level+1) )

        return ans
