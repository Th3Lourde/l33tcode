'''
Given a binary tree root,

a node in a tree is named
good if the path from root to X
contains no nodes creater than x

return the number of good nodes
in the binary tree

Use a stack, have the max element seen
on the path so far

            3
          1   4
        3    1  5


[ [3, 3] ]
   ^  ^
   node max

if node.val >= max:
    ans += 1

stack.append([node[0].left, max(node[0].val, node[1])])
stack.append([node[0].right, max(node[0].val, node[1])])

return ans

Got it right.
'''

class Solution:
    def goodNodes(self, root):
        stack = [ [root, root.val] ]
        ans = 0

        while stack:
            node = stack.pop()

            if node[0]:
                if node[0].val >= node[1]:
                    ans += 1

                stack.append([node[0].left, max(node[0].val, node[1])])
                stack.append([node[0].right, max(node[0].val, node[1])])

        return ans
