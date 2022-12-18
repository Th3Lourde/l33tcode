import heapq

'''
    1
 3  2  4
5 6

maxDepths=[2,1]
maxDiam=2

dfs(1)
    1,2=dfs(3)
        0,0=dfs(5)
        0,0=dfs(6)
    0,0=dfs(2)
    0,0=dfs(4)
'''

class Solution:
    def diameter(self, root):
        def dfs(node):
            maxDepths = [0]
            maxDiam = 0

            for n in node.children:
                depth, diam = dfs(n)

                maxDiam = max(maxDiam, diam)

                heapq.heappush(maxDepths, depth+1)

                if len(maxDepths) > 2:
                    heapq.heappop(maxDepths)

            return max(maxDepths), max(maxDiam, sum(maxDepths))

        _, maxDiam = dfs(root)

        return maxDiam
