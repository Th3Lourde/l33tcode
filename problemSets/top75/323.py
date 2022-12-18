
class Solution:
    def countComponents(self, n, edges):
        seen = set()
        adj = {}
        ans = 0

        for i in range(n):
            adj[i] = set()

        for l,r in edges:
            adj[l].add(r)
            adj[r].add(l)

        def dfs(node):
            seen.add(node)

            for adjNode in adj[node]:
                if adjNode not in seen:
                    dfs(adjNode)

        for node in range(n):
            if node not in seen:
                ans += 1
                dfs(node)

        return ans
