'''
Given the root of a binary tree, the value of a target node target
and an integer k, return an array of the values of all ndoes that
have a distance k from the target node

What if we make this a graph, and then we can traverse the graph
k times and return all nodes that we see.
'''

class Solution:
    def distanceK(self, root, target, k):
        adjList = {}

        def createGraph(node, parent):
            neighbors = []

            if parent:
                neighbors.append(parent.val)

            if node.left:
                neighbors.append(node.left.val)
                createGraph(node.left, node)

            if node.right:
                neighbors.append(node.right.val)
                createGraph(node.right, node)

            adjList[node.val] = neighbors

        createGraph(root, None)

        seen = set({target.val})
        traversalList = [target.val]

        for _ in range(k):
            newTraversalList = []

            for node in traversalList:
                adjNodes = adjList[node]

                for n in adjNodes:
                    if n not in seen:
                        seen.add(n)
                        newTraversalList.append(n)

            traversalList = newTraversalList

        return traversalList
