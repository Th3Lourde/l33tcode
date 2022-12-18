
# https://leetcode.com/problems/network-delay-time/discuss/471164/Python-DFS-BFS-Dijkstra-Bellman-Ford-SPFA-Floyd-Warshall
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, heap = [0] + [float("inf")] * N, defaultdict(list), [(0, K)] # it's a min-heap
        for u, v, w in times:
            graph[u].append((v, w))
        while heap:
            time, node = heapq.heappop()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    heapq.heappush(heap, (time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1


# https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concise
class Solution(object):
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] # distance, row, col
        DIR = [0, 1, 0, -1, 0]

        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]: continue  # this is an outdated version -> skip it
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right

            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))
