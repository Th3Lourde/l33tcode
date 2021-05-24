'''
Clone Graph
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Ok so how can we do this?

Create a new node, then make a recursive call on the neighbors.
Maybe have a set of nodes that we have seen to avoid double counting?


'''

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None


        nodeToNeighbors = {}

        stack = [(node)]

        while stack:
            node = stack.pop()

            if node.val not in nodeToNeighbors:
                nodeToNeighbors[node.val] = set()

            for n in node.neighbors:
                nodeToNeighbors[node.val].add(n.val)

                if n.val not in nodeToNeighbors:
                    stack.append(n)

        valToNode = {}

        for key in nodeToNeighbors.keys():
            valToNode[key] = Node(key)

        ans = None

        for key in valToNode.keys():
            for neigh in nodeToNeighbors[key]:
                valToNode[key].neighbors.append(valToNode[neigh])
            ans = key

        return valToNode[1]
