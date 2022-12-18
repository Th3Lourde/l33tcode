import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        nodeToTime = [0] + [float('inf')] * n
        graph = {}
        heap = [(0,k)]

        for i in range(1,n+1):
            graph[i] = []

        for start, end, cost in times:
            graph[start].append((end, cost))

        while heap:
            time, node = heapq.heappop(heap)

            if time < nodeToTime[node]:
                nodeToTime[node] = time

                for end, cost in graph[node]:
                    heapq.heappush(heap, (time+cost, end))

        mx = max(nodeToTime)

        return mx if mx < float('inf') else -1




print(Solution().networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 3, 1))


print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1))
print(Solution().networkDelayTime([[1,2,1]], 2, 1))
print(Solution().networkDelayTime([[1,2,1]], 2, 2))
