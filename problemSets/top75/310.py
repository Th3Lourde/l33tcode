from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        graph = {}

        for node in range(n):
            graph[node] = set()

        for l,r in edges:
            graph[l].add(r)
            graph[r].add(l)

        while len(graph) > 2:
            # Find all leaf nodes
            leafs = set()

            for key in graph:
                if len(graph[key]) == 1:
                    leafs.add(key)

            for leaf in leafs:
                # Remove the neighbor of leaf
                neigh = graph[leaf].pop()

                # delete leaf from graph
                graph[neigh] = graph[neigh] - set({leaf})

                del graph[leaf]

        return list(graph.keys())



print(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
