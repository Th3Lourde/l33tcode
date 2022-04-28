
from collections import deque

# Does it matter where we start?
# Do we really need to test the scenario where the initial node
# is of type a or type b?
class Solution:
    def isBipartite_1(self, graph):
        self.bipartite = False
        self.visited = set()
        self.Aset = set()
        self.Bset = set()
        self.n = 0

        for idx in range(len(graph)):
            if len(graph[idx]) > 0:
                self.n += 1

        if self.n == 0:
            return True

        def dfs(node):
            if node in self.visited:
                return

            # Get adjacent nodes
            adjNodes = graph[node]
            holds = True

            if node in self.Aset:
                # Assert that each other node must be in Bset
                # If this holds, continue the traversal
                # Else break

                for adjNode in adjNodes:
                    # I believe this breaks for the first lc case
                    # if adjNode in visited:
                    #     continue

                    if adjNode in self.Aset:
                        # print("{} is in Aset".format(adjNode ))
                        holds = False
                        break

                    self.Bset.add(adjNode)

            else:
                # Assert that each other node must be in Aset
                for adjNode in adjNodes:
                    # if adjNode in visited:
                    #     continue

                    if adjNode in self.Bset:
                        # print("{} is in Bset".format(adjNode ))
                        holds = False
                        break

                    self.Aset.add(adjNode)


            if holds:
                self.visited.add(node)

                # print("Visited: {}".format(self.visited))
                # print("len(Visited): {}".format(len(self.visited)))
                # print("len(graph): {}".format(len(graph)))
                # print("Aset: {}".format(self.Aset))
                # print("Bset: {}".format(self.Bset))

                if len(self.visited) == self.n:
                    self.bipartite = True
                    return

                for adjNode in adjNodes:
                    dfs(adjNode)

        for node in range(len(graph)):
            if node in self.visited:
                continue

            dfs(node)

        return self.bipartite

    def isBipartite_2(self, graph):
        color = {}

        def dfs(node):
            for i in graph[node]:
                if i in color:
                    if color[i] == color[node]:
                        return False
                else:
                    color[i] = 1 - color[node]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False

        return True

    def isBipartite(self, graph):
        color = {}

        def dfs(node):
            # 1) Test all adjancent nodes
            # |--> If an adj node is in the dictionary, test if it satisfies the condition
            # |--> If it isn't, make a recursive call, if it fails return false
            for adjNode in graph[node]:
                if adjNode in color:
                    if color[node] == color[adjNode]:
                        return False
                else:
                    color[adjNode] = 1 - color[node]

                    if not dfs(node):
                        return False
            return True


        for node in range(len(graph)):
            if node not in color:
                color[node] = 0

                if not dfs(node):
                    return False

|        return True

print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])) # false
print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]])) # true
print(Solution().isBipartite([[4],[],[4],[4],[0,2,3]])) # true
print(Solution().isBipartite([[1],[0],[4],[4],[2,3]])) # true
print(Solution().isBipartite([[],[],[]])) # true
print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2],[5,6,7],[4,6],[4,5,7],[4,6]])) # true
