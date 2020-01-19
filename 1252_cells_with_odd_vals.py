
class Solution:
    def oddCells(self, n, m, indices):
        '''
        '''
        row = [0]*n
        col = [0]*m

        for i in range(len(indices)):
            row[indices[i][0]] += 1
            col[indices[i][1]] += 1

        ans = 0

        for i in range(len(row)):
            for j in range(len(col)):
                if (row[i]+col[j])%2 != 0:
                    ans += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    n = 2
    m = 3
    indices = [[0,1],[1,1]]

    print(s.oddCells(n, m, indices))

    print(s.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))
