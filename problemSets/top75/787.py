'''
There are n cities connected by some number of flights. You are given an array
flights where flight[i] = [start, end, cost]

n represents the number of nodes

you are also given three ints, start, end, k

return the flight with the min cost

so I think this is dijkstra's algo

let's maintain a heap with elements of the following form:
- (cost, node, jumpsLeft, visited)

we will also need to create a dict that we can use to figure
out where we can go (and the cost of going there)

since it's a min heap, the flight that has the minimum cost
will be a priority and will finish first. So the first time
we hit our destination, we quit.



'''

import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = {}

        for node in range(n):
            adj[node] = []

        for start, end, cost in flights:
            # print(start)
            adj[start].append((end, cost))

        # print(adj)
        # for a in adj:
        #     print("{}-->{}".format(k, adj[a]))

        heap = [(0, src, k, set({src}))]

        while heap:
            cost, node, jumpsLeft, visited = heapq.heappop(heap)

            if node == dst:
                return cost

            if jumpsLeft >= 0:
                for newNode, newCost in adj[node]:
                    # print("{}|{}".format(newNode, newCost))
                    if newNode not in visited:
                        # visited.add(newNode)
                        # either perform union with new set, don't want the visited of
                        # one traversal interfering with the traversal of another
                        heapq.heappush(heap, (cost+newCost, newNode, jumpsLeft-1, set(visited)))
                        # visited.remove(newNode)

        return -1

flights = [
 [0, 4, 2],
 # [1, 0, 4],
 # [1, 2, 6],
 # [1, 5, 4],
 # [1, 7, 6],
 # [1, 9, 1],
 # [2, 5, 6],
 # [3, 4, 4],
 # [4, 0, 9],
 # [4, 1, 5],
 # [4, 7, 10],
 # [5, 2, 4],
 # [5, 9, 1],
 [6, 2, 10],
 [6, 5, 8],
 [6, 8, 6],
 [7, 0, 5],
 [7, 2, 8],
 [7, 4, 4],
 [7, 8, 10],
 [7, 9, 4],
 [8, 7, 3],
 [9, 6, 5],
 # [9, 7, 3]
]

print(Solution().findCheapestPrice(10, flights, 6, 0, 7))

t = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]

t.sort()
t

print(Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 2, 5))

10
[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
6
0
7

a = {"a": [(1,2), (3,4)]}

for z,d in a["a"]:
    print("{}|{}".format(z,d))
