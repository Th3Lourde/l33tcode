'''
Given the root of a binary tree with N nodes,
each node in the tree has node.val coints,
and there are N coints total.

Loop through tree. If we hit a node w/out any vals,
store it?

The trouble is that we can't go backwards, we can only
go down.

If a node has more than one coin, do something
If a node doesn't have any coins, do something

Yea I was making it too complicated.

A node has coins (or has zero coins).

We return the .val + left traversal + right traversal - 1

Our goal is to return the number of moves required to balance the
tree and all of the subtrees.

.val is the number of coins that we currently have.
left traversal is the number of moves that left needs
right traversal is the number of moves that right needs
-1 reduces the magnitude in the case we have anything positive.


'''

class Solution:

    resp = 0
    def distributeCoins(self, root):
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.resp += abs(left) + abs(right)
            return node.val + left + right - 1

        dfs(root)
        return self.resp
