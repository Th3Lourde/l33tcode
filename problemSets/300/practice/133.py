"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Idea:
Traverse through the graph, create a mapping for oldToNode

Create a new mapping newToNode

1 --> 2
|     |
|     |
4 --> 3

# Loop through graph, create oldToNode dict

oldToNode: {
    1: Node(1, [2,4]),
    2: Node(2, [1,3]),
    4: Node(4, [1,3]),
    3: Node(3, [4,2]),
}

# Loop through oldToNode dict, create v1 of newToNode dict

newToNode: {
    1: Node(1, []),
    2: Node(2, []),
    4: Node(4, []),
    3: Node(3, []),
}

loop through newToNode dict
    query oldToNode dict and loop through parents and add accordingly
'''

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        oldToNode = {}
        newToNode = {}

        def mapGraph(node):
            if not node or node.val in oldToNode:
                return

            oldToNode[node.val] = node

            for adjNode in node.neighbors:
                mapGraph(adjNode)

        mapGraph(node)

        for key in oldToNode:
            node = Node(val=key)
            newToNode[key] = node

        for key in newToNode:
            for adjNode in oldToNode[key].neighbors:
                newToNode[key].neighbors.append(newToNode[adjNode.val])

        return newToNode[1]
