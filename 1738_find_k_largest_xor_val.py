import heapq as h

class Solution:
    def kthLargestValue(self, matrix, k):
        heap = []

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if i:
                    cell ^= matrix[i-1][j]
                if j:
                    cell ^= matrix[i][j-1]
                if j and i:
                    cell ^= matrix[i-1][j-1]

                matrix[i][j] = cell

                h.heappush(heap, -1*cell)
                    


        for _ in range(k):
            h.heappop(heap)

        return -1*h.heappop(heap)

if __name__ == '__main__':
    s = Solution()

    print(s.kthLargestValue([[5,2],[1,6]], 1))
