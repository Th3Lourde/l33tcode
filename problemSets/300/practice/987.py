from collections import deque

class Solution:
    def verticalTraversal(self, root):
        idx_to_vals = {}
        min_col = 0
        q = deque([(root, 0,0)])

        while q:
            node, row, col = q.pop()

            min_col = min(min_col, col)

            if col in idx_to_vals:
                idx_to_vals[col].append((row, node.val))
            else:
                idx_to_vals[col] = [(row, node.val)]

            if node.left:
                q.appendleft((node.left, row+1, col-1))

            if node.right:
                q.appendleft((node.right, row+1, col+1))

        print(idx_to_vals)

        for idx in idx_to_vals:
            # List of (row, val)
            # For all elements that have the same row,
            tuple_list = idx_to_vals[idx]
            sorted_list = []
            l=0

            # Look right, if element right of current element has same value row
            while l < len(tuple_list):
                if l < len(tuple_list)-1 and tuple_list[l][0] == tuple_list[l+1][0]:
                    r = l
                    tmp_list = []

                    while r < len(tuple_list) and tuple_list[r][0] == tuple_list[l][0]:
                        tmp_list.append(tuple_list[r][1])
                        r += 1

                    tmp_list.sort()
                    sorted_list = sorted_list + tmp_list
                    l = r

                else:
                    sorted_list.append(tuple_list[l][1])
                    l += 1

            idx_to_vals[idx] = sorted_list

        resp = []

        while min_col in idx_to_vals:
            resp.append(idx_to_vals[min_col])
            min_col += 1

        return resp



def test():
    dict_tuple = {0: [(0, 0), (2, 10), (2, 2), (4, 4), (6, 6)], -1: [(1, 7), (3, 11), (3, 3), (5, 12), (7, 8)], 1: [(1, 1), (3, 14), (5, 5)], -2: [(4, 13)], 2: [(6, 9)]}
