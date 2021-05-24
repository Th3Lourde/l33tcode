class Solution:
    # Solution is technically correct, TLE
    # going to leave it here until I actually
    # understand the non-tle answer
    def criticalConnections(self, n, connections):
        critical = []
        graph = {}

        for i in range(n):
            graph[i] = []

        for l,r in connections:
            graph[l].append((l,r))
            graph[r].append((l,r))

        # print(graph)

        def findCycle(target, node, path):
            for e in graph[node]:
                if e not in path:
                    path.add(e)

                    if target in e:
                        return path

                    nextNode = e[0] if e[0] != node else e[1]

                    cycleFound = findCycle(target, nextNode, path)

                    if cycleFound:
                        return cycleFound

                    path.remove(e)

            return set()

        cycles = set()

        for l,r in connections:
            if (l,r) not in cycles:
                # print("({},{})".format(l,r))
                cycle = findCycle(l, r, set({(l, r)}))

                # print(cycle)

                if len(cycle) == 0:
                    critical.append([l,r])

                else:
                    cycles = cycles.union(cycle)

        return critical

s = Solution()

print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
print(s.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))
