from collections import deque

class Solution:
    def validTree(self, n, edges):
        nodeToEdges = {}

        for i in range(n):
            nodeToEdges[i] = []

        for a,b in edges:
            nodeToEdges[a].append(b)
            nodeToEdges[b].append(a)

        q = deque([(0,None)])
        seen = set()
        nodes = 0

        while q:
            node, parent = q.pop()

            nodes += 1

            if node in seen:
                return False

            seen.add(node)

            for adj in nodeToEdges[node]:
                if adj != parent:
                    q.appendleft((adj, node))

        return nodes == n 
