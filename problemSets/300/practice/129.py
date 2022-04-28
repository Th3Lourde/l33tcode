'''
You are given the root of a binary tree containing
digits from 0-9.

Each root to leaf path in the tree represents a number.

Return the total sum of all root-to-leaf numbers.

Ok so perform bfs to minimize the number of times we
redundantly touch a given node.

        4
      9   0
     5 1

ans = 40

[5, ['4', '9', '1']]
[1, ['4', '9']]


'''

from collections import deque

class Solution:
    def sumNumbers(self, root):
        ans = 0
        q = deque([[root, []]])

        while q:
            node, sumArr = q.pop()
            sumArr.append(str(node.val))

            if not node.left and not node.right:
                strRepr = "".join(sumArr)
                ans += int(strRepr )

            if node.left:
                q.appendleft([node.left, list(sumArr)])

            if node.right:
                q.appendleft([node.right, list(sumArr)])

        return ans
