'''
Return the sum of the the nodes with an even-valued
grandparent.

One way to do this is to traverse through a tree:
if a node has an even value, see if it has a grandchild
if it does, add val of grandchild to sum.

One function for traverse, another to find grand children

given a node, find grandchildren, and return their sum.

node

# get children:
children = []

if node.left:
    children.append(node.left)

if node.right:
    children.append(node.right)

ans = 0

for child in children:
    if child.left:
        ans += child.left.val

    if child.right:
        ans += child.right.val

return ans

'''

class Solution:
    def sumEvenGrandparent(self, root): # works

        def sumGrandchildren(node, ans):
            children = []

            if node.left:
                children.append(node.left)

            if node.right:
                children.append(node.right)

            for child in children:
                if child.left:
                    ans += child.left.val

                if child.right:
                    ans += child.right.val

            return ans

        ans = 0

        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if node.val % 2 == 0:
                    # node is even, sum grandchildren
                    sumGrandchildren(node, ans)

                stack.append(node.right)
                stack.append(node.left)

        return ans
