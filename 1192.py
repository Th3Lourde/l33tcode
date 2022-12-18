'''
Ok so this is an algo that we know or
we don't know. All good.

What we want to do is find all edges
where the only way to get from the first node
to the second is via the edge that we have.

Thus, if there is no other way to get to the
destination node from the beginning node other
than this edge, this edge is a critical connection.

So we have these different variables:
- ans
|--> list of critical connections
- timer
|--> Is incremented every time we make a dfs call
- used
|--> Keeps track if we have seen a node or not
- tin
|--> tin[node] is the time at which we visited node
- low
|--> low[node] is the min between
|--> the time when we first reached node
|--> the time when we reached any child 1 step away from node
'''

from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        used, tin, low = [0]*n, [-1]*n, [-1]*n
        self.timer, ans = 0, []
        graph = defaultdict(list)

        def dfs(node, par=-1):
            used[node] = 1
            self.timer += 1
            tin[node] = low[node] = self.timer

            for child in graph[node]:
                if par == child:
                    continue
                elif used[child] == 1:
                    low[node] = min(low[node], tin[child])
                else:
                    dfs(child, node)
                    low[node] = min(low[node], low[child])
                    if low[child] > tin[node]: ans.append([child, node])



        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        for i in range(n):
            if not used[i]: dfs(i)

        return ans




print(Solution().criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))
print(Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
print(Solution().criticalConnections(1, [[0,1]]))
