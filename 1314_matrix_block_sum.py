'''
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

Ok so this problem is a bit trickier than I thought.

This is supposed to be dp, what's the best way to go through this?

One solution would be to brute-force the first element in every column.

If we don't do that we'd have to keep track of elements that have/haven't
been used, etc...

We could instead create a list of [i-K, i-K+1, ..., i, ...]

It would probably be better to expand the input accordingly and surround it
with zeros. Have a range of i/j values to calculate for, execute.

That way we never need to worry about out of bounds errors


  [0,0,0,0,0]

[0]+[1,2,3]+[0]
[0]+[4,5,6]+[0]
[0]+[7,8,9]+[0]

  [0,0,0,0,0]

1) For each row, insert/append [0]*k
2) Create top/bottom rows, size of len(mat[0]) + k * 2. Insert at zero, append

When working on the rows, store the last element. No. Just do the index math and
subtract it.

Ok so that took a while to write out, part of the challenge was that I didn't
fully understand the problem until I had already attempted a couple of trys.

Also I'm not really sure that this is DP. We are just calculating the perim
and going from there.

Let's look at a solution, implement it, and move forwards.


'''


# Version 1
# Took a long time to write-out. P
class Solution1:
    # [rowS, rowE), [colS, colE)
    def matSum(self, mat, start, end):
        ans = 0

        for row in range(start, end):
            for col in range(start, end):
                ans += mat[row][col]

        return ans

    def matrixBlockSum(self, mat, K):
        ans = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]

        # 0) Add zeros to the matrix
        tmp = [0]*K

        for i in range(len(mat)):
            mat[i] = tmp + mat[i] + tmp

        tmp = [0]*(len(mat[0]))

        for i in range(K):
            mat.insert(0, tmp)
            mat.append(tmp)

        # for row in mat:
        #     print(row)
        # print()

        # return

        for row in range(K, len(mat)-K):
            # minus top-k-most element, plus bottom-k-most element

            if row == K:
                ans[0][0] = self.matSum(mat, K, K+K+1)
            else:
                # print("row-K: {} | row-K-1: {} | row-1-K: {} | row+K: {}".format(row-K, row-K-1, row-1-K, row+K))
                # print("a: {} b: {} c: {}".format(ans[row-K-1][0], mat[row-1-K][K], mat[row+K][K]))
                # minus top value we are losing, add bottom value we are gaining, add current row up to k
                ans[row-K][0] = ans[row-K-1][0] - sum(mat[row-1-K][K:K+K+1]) + sum(mat[row+K][K:K+K+1])
                # print(ans[row-K][0])

            for col in range(K+1, len(mat[0])-K):
                prevRow = 0
                newRow = 0

                # print("start: {}, end: {}".format(row, row+K+1))

                for r in range(row-K, row+K+1):
                    prevRow += mat[r][col-K-1]
                    newRow += mat[r][col+K]

                # print("prev row: {}".format(prevRow))
                # print("new row: {}".format(newRow))

                ans[row-K][col-K] = ans[row-K][col-K-1] - prevRow + newRow


        for row in ans:
            print(row)


# Version 2 (after I looked at the solution)
'''
So the trick here is to realize that you can solve all of the
problems via different rectangles (summed), where the sum starts
at the top left coordinate.

So you calculate all of your sums once, then record every answer
as the addition/subtraction of different sums.


'''

class Solution:
    def matrixBlockSum(self, mat, K):

        dp =  [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        ans = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]

        rows = len(mat)-1
        cols = len(mat[0])-1

        # 0) Create prefix sum
        for row in range(len(mat)):
            sigma = 0

            for col in range(len(mat[0])):
                sigma += mat[row][col]

                dp[row][col] = sigma

                if row > 0:
                    dp[row][col] += dp[row-1][col]


        for row in range(len(mat)):
            for col in range(len(mat[0])):

                min_row, max_row = max(0, row-K), min(rows, row+K)
                min_col, max_col = max(0, col-K), min(cols, col+K)

                ans[row][col] = dp[max_row][max_col]

                if min_row > 0:
                    ans[row][col] -= dp[min_row-1][max_col]

                if min_col > 0:
                    ans[row][col] -= dp[max_row][min_col-1]

                if min_row > 0 and min_col > 0:
                    ans[row][col] += dp[min_row-1][min_col-1]

        return ans











if __name__ == '__main__':
    s = Solution()

    eg = [
    [31,2,4,33,5,36],
    [12,26,9,10,29,25],
    [13,17,21,22,20,18],
    [24,23,15,16,14,19],
    [30,8,28,27,11,7],
    [1,35,34,3,32,6],
    ]

    s.matrixBlockSum(eg, 1)


    #
    # s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1)
    # s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 2)
