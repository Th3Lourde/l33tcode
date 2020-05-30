
'''
Given BT, find it's minimum depth.
That is, return the number of nodes
present in the path to the first leaf node.
bfs,

     3
    / \
   9  20
      / \
     15  7

bfs(None)
q = [3]
q = [], 3 if 3.left and 3.right, q = [3.left, 3.right] + q
        else: return 3.

        if not 3.left and not 3.right, return 3
        else:  q = [3.left, 3.right] + q

---------------------------------------------------------------------------

bfs()
q = [ [3, (1)] ]

q =  [], node = [3, (1)]

    if not node[0].left and not node[0].right, return node[1]
    else:  q = [[node[0].left, node[1]+1, [node[0].right, node[1]+1] + q


q = [ [3, (1)] ]
q = [ [9, (2)], [20, (2)] ]
q = [ [15, (3)], [7, (3)] ]
[9, (2)]

'''


class Solution:
    def minDepth(self, root): # Works very well, used bfs.

        if not root:
            return 0

        q = [[root, 1]]

        while q:
            node = q.pop()

            if node[0]:
                if not node[0].left and not node[0].right:
                    return node[1]

                else:
                    q = [ [node[0].left, node[1]+1], [node[0].right, node[1]+1] ] + q



    def minDepth_1(self, root): # Also works, slower.

        if not root:
            return 0

        min_nodes = None
        stack = [ [root, 1] ]

        while stack:
            node = stack.pop()

            if node[0]:
                if not node[0].left and not node[0].right:

                    if min_nodes:
                        min_nodes = min(min_nodes, node[1])

                    else:
                        min_nodes = node[1]

                else:
                    stack.append([node[0].left, node[1]+1])
                    stack.append([node[0].right, node[1]+1])

        return min_nodes
