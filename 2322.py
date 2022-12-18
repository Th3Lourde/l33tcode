from collections import defaultdict

class Solution:
    def minimumScore(self, nums, edges):
        N = len(nums)

        adj = defaultdict(list)

        # Create adjacency mapping
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # For each node, calculate the xOr

        nodeToXor = [0]*N

        def dfs(node, p):
            current = nums[node]

            for v in adj[node]:
                if v != p:
                    current ^= dfs(v, node)

            nodeToXor[node] = current
            return current

        dfs(0, -1)

        print(nodeToXor)

        # Create node --> descendents mapping
        parentToDescendents = [set() for _ in range(N)]

        def genParents(node, p):
            parentToDescendents[node] = set([node])

            for v in adj[node]:
                if v != p:
                    parentToDescendents[node] |= genParents(v, node)

            return parentToDescendents[node]

        genParents(0, -1)

        # Now
        best = float('inf')
        for i in range(1, N):
            for j in range(i+1, N):
                if j in parentToDescendents[i]:
                    a = nodeToXor[0] ^ nodeToXor[i]
                    b = nodeToXor[i] ^ nodeToXor[j]
                    c = nodeToXor[j]
                    best = min(best, max(a,b,c) - min(a,b,c))
                elif i in parentToDescendents[j]:
                    a = nodeToXor[0] ^ nodeToXor[j]
                    b = nodeToXor[j] ^ nodeToXor[i]
                    c = nodeToXor[i]
                    best = min(best, max(a,b,c) - min(a,b,c))
                else:
                    a = nodeToXor[0] ^ nodeToXor[i] ^ nodeToXor[j]
                    b = nodeToXor[i]
                    c = nodeToXor[j]
                    best = min(best, max(a,b,c) - min(a,b,c))

        return best

print(Solution().minimumScore([9,14,2,1], [[2,3],[3,0],[3,1]]))

print(Solution().minimumScore([1,5,5,4,11], [[0,1],[1,2],[1,3],[3,4]]))
