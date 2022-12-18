'''
Given a reference of a node in a connected undirected graph
Return a deep copy of the graph

Ok so we just need to create a new graph with the same neighbors

We can have a graph we

1 --- 2
|     |
|     |
4 --- 3


1 : Node(1)
2 : Node(2)
3 : Node(3)
4 : Node(4)


Perform the first traversal to create all of the nodes
that we need to create

Then perform a second traversal to add all neighbors

Then return the dict value for the node.val we are given
'''

from collections import deque

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        valToNode = {}
        q = deque([node])

        while q:
            n = q.pop()

            if n.val not in valToNode:
                valToNode[n.val] = Node(n.val)

                for neighb in n.neighbors:
                    if neighb.val not in valToNode:
                        q.appendleft(neighb)

        q = deque([node])

        while q:
            n = q.pop()

            if len(n.neighbors) != len(valToNode[n.val].neighbors):
                for neigh in n.neighbors:
                    lookupVal = neigh.val
                    valToNode[n.val].neighbors.append(valToNode[lookupVal])

                    q.appendleft(neigh)

        return valToNode[node.val]
