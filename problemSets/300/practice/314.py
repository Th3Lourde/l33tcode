'''
min_column = -1

-1    0       1
[9]  [3,15]  [20]

dfs(7,2)
'''

from collections import deque

class Solution:
    # ok so mostly correct, do level order traversal instead and we should be good?
    def verticalOrder(self, root):
        if not root: return []

        self.column_to_row = {}
        self.min_column = float('inf')

        # def dfs(node, column):
        #     self.min_column = min(self.min_column, column)
        #
        #     if column in self.column_to_row:
        #         self.column_to_row[column].append(node.val)
        #     else:
        #         self.column_to_row[column] = [node.val]
        #
        #     if node.left:
        #         dfs(node.left, column-1)
        #
        #     if node.right:
        #         dfs(node.right, column+1)
        #
        # dfs(root, 0)

        q = deque([(root,0)])

        while q:
            node, column = q.pop()

            self.min_column = min(self.min_column, column)

            if column in self.column_to_row:
                self.column_to_row[column].append(node.val)
            else:
                self.column_to_row[column] = [node.val]

            if node.left:
                q.appendleft([node.left, column-1])

            if node.right:
                q.appendleft([node.right, column+1])

        resp = []

        while self.min_column in self.column_to_row:
            resp.append(self.column_to_row[self.min_column])
            self.min_column += 1

        return resp
