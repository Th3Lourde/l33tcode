'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf
path such that adding up all the values along the path equals the given sum.

Use bfs in in order to get all sums. If one of the sums equal our target
return True, else False

'''

class Solution:
    def hasPathSum(self, root, sum): # This works. Using a stack is better than using a queue.
        if not root: # Assuming that a path needs to have more than two nodes in it.
            return False

        q = [[root, 0]]

        while q:

            node = q.pop()

            if node[0]:
                tmp = node[1] + node[0].val


                if not node[0].left and not node[0].right and tmp == sum:
                    return True

                q.append([node[0].left, tmp])
                q.append([node[0].right, tmp])

        return False
