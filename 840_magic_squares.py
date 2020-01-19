


class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        ans = 0

        for i in range(len(grid)):
            print(grid[i])

        '''
        Don't actually need grid to be sqr
        only need grid to have more than 3 rows
        and more than 3 columns
        '''

        # Make sure grid is big enough to contain
        # a `magic` square
        if len(grid) < 3 or len(grid[0]) < 3:
            return ans

        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):

                terms = {}

                t = False

                a = grid[i][j] + grid[i][j-1] + grid[i][j-2]
                b = grid[i-1][j] + grid[i-1][j-1] + grid[i-1][j-2]
                c = grid[i-2][j] + grid[i-2][j-1] + grid[i-2][j-2]

                d = grid[i][j] + grid[i-1][j] + grid[i-2][j]
                e = grid[i][j-1] + grid[i-1][j-1] + grid[i-2][j-1]
                f = grid[i][j-2] + grid[i-1][j-2] + grid[i-2][j-2]

                g = grid[i][j-2] + grid[i-1][j-1] + grid[i-2][j]
                h = grid[i-2][j-2] + grid[i-1][j-1] + grid[i][j]

                if (a == b) and (b == c) and (c == d) and (d == e) and (e == f) and (f == g) and (g == h):
                    # print("hi")

                    print("{} {} {}".format(grid[i-2][j-2], grid[i-2][j-1], grid[i-2][j]))
                    print("{} {} {}".format(grid[i-1][j-2], grid[i-1][j-1], grid[i-1][j]))
                    print("{} {} {}".format(grid[i][j-2], grid[i][j-1], grid[i][j]))


                    ans += 1
                    t = True

                    # Search the matrix to make sure that all of the terms are unique
                    # AND that they are all within the bounds

                    for z in range(i-2, i+1):
                        for k in range(j-2, j+1):

                            try:
                                # Don't have repeat
                                terms[grid[z][k]] += 1

                                    # Is grid[z][k] not in [1,9] and have we added to ans
                                    # This check should not go here
                                if not((grid[z][k] >= 1) and (grid[z][k] <= 9)) and (t):

                                    ans -= 1
                                    t = False
                                    break

                            except:
                                terms[grid[z][k]] = 0

                                if not((grid[z][k] >= 1) and (grid[z][k] <= 9)) and (t):

                                    ans -= 1
                                    t = False
                                    break

                            if terms[grid[z][k]] != 0 and t:
                                ans -= 1
                                t = False
                                break


        if ans < 0:
            return 0
        else:
            return ans

if __name__ == '__main__':
    t1 = [[4,3,8,4],
          [9,5,1,9],
          [2,7,6,2]]


    t2 = [[1,1,1],[4,5,6],[9,9,9]]

    t3 = [[5,5,5],[5,5,5],[5,5,5]]

    t4 = [[10,3,5],[1,6,11],[7,9,2]]

    t5 = [[9,0,8,1,6],[2,4,3,5,7],[4,3,4,9,2],[2,4,5,6,1],[9,8,0,7,8]]

    t6  = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]

    t7 = [[10,3,5],[1,6,11],[7,9,2]]

    s = Solution()
    # r = s.numMagicSquaresInside(t1)
    # r = s.numMagicSquaresInside(t2)
    # r = s.numMagicSquaresInside(t3)
    # r = s.numMagicSquaresInside(t4)
    # r = s.numMagicSquaresInside(t5)
    # r = s.numMagicSquaresInside(t6)
    r = s.numMagicSquaresInside(t7)



    print(r)
