import heapq

class Solution:
    def minimumEffortPath(self, heights):
        heap = [(0,0,0)]
        r, c = len(heights), len(heights[0])
        seen = [[float('inf')] * c for _ in range(r)]
        seen[0][0] = 0

        while heap:
            cost, row, col = heapq.heappop(heap)

            if (row,col) == (r-1, c-1):
                return cost

            for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if 0 <= nrow < r and 0 <= ncol < c:
                        localCost = max(cost, abs(heights[row][col] - heights[nrow][ncol]))
                        if localCost < seen[nrow][ncol]:
                            heapq.heappush(heap, (localCost, nrow, ncol))
                            seen[nrow][ncol] = localCost

        return






print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))


print(Solution().minimumEffortPath([[3]]))

print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))

print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
