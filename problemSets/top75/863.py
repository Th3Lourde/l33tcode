'''
Given the root of a binary tree,
the value of a target node target and
an integer k,

return an array of the values of all nodes that
have a distance k from the target node.

Ok so this problem is pretty difficult if we need
to keep things as a tree.

If we can change it to a graph however, we can just
bfs from the target and boom there's our answer.

Let's just do that.
'''

from collections import defaultdict
from collections import deque

class Solution:
    def distanceK(self, root, target, k):
        if k == 0:
            return [target.val]

        adj = defaultdict(list)

        def populateAdj(node):

            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                populateAdj(node.left)

            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                populateAdj(node.right)

        populateAdj(root)

        # print(adj)

        itrs = k
        q = deque([target.val])
        seen = set()

        while itrs > 0:
            newQ = deque()

            # print(q)

            while q:
                node = q.pop()

                if node in seen:
                    continue

                seen.add(node)

                for adjNode in adj[node]:
                    if adjNode not in seen:
                        newQ.appendleft(adjNode)

            itrs -= 1
            q = newQ

        return list(q)
