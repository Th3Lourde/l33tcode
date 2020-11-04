'''
Given a directed acyclic graph
of N nodes, find all possible
paths from node at idx 0 to
node n-1

'''

class Solution:
    def allPathsSourceTarget(self, graph):

        ans = []

        stack = [ (0, [0]) ]

        end = len(graph)-1

        while stack:

            idx, path = stack.pop()

            if idx == end:
                ans.append(path)

            for node in graph[idx]:
                stack.append((node, path + [node]))

        return ans
