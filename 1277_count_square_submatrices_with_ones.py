'''
Given a matrix of ones and zeros, return
how many square submatrices have all ones.

Ok so I'm pretty sure that I solved this problem,
however the solution that I came up with isn't
optimal.

What might be a better way to do this?

Ok so we can start with what we have to do in order
to solve this problem. We need to cycle through the
different square sizes and validate whether or not
the squares contain all ones.

Instead of iterating through all possible square sizes,
we could instead start at each element that has a one,
and test to see if squares of larger sizes are valid
at the square that we are currently at.

So loop through all of the elements,
if mat[i][j] == 1:
    ans += itr(mat[i][j])

Where itr would be a function that
takes in a coordinate with a value
of one and returns the number of squares
that have that element as the top-right
element.

resp = 0
sqr = True
sz = 1

while sqr:
    # check vals from coord + sz-1
    # if any of them are zeros,
    # set sqr = False

    # else, resp += 1, sz += 1


I think that this method would have less
checks.

Let's write out what we have, then think
through itr() more.

Ok so we would like to check the needed
rows/columns. Every iteration we are
doing a check of the outermost col/row.

so if we start at [0,0], we first want to
go 1 out, then two, then three

Check bottom row first.

There is also an inefficiency, as we
are checking multiple values more than
once. Maybe we could be adding one to
row and col as we go, and then meeting
in the middle?

Ok, so add one to row and col initially.
Then, subtract one from row, col, until they
are equal, so we should probably make a copy
by reference and go from there

def itr(row, col):
    ans = 0
    sqr = True
    sz = 1

    while sqr:

        r = row
        c = col

       while r <= row+sz and c <= col+sz:
            if not (matrix[r][col] == matrix[row][c] == 1):
                return ans

            r += 1
            c += 1

        # We have stepped through a valid square, time to
        # move on to the next square

        ans += 1




Ok so I was wrong in my assumption that we were double counting.
Since our starting point is always being updated by the size
parameter, we will not actually end up double counting.


def itr(row, col):
    ans = 0
    sz = 0

    while True:
        # Assuming that we have valid search
        # dimensions.

        # Iterate through the bottom most
        # row, hit the 'last' element
        # Bottom search
        for i in range(col, col+sz+1):
            if matrix[row+sz][i] != 1:
                return ans

        # Iterate through the right most column
        # skip the last element
        # Far right search
        for i in range(row, row+sz):
            if matrix[i][col+sz] != 1:
                return ans

        # When have gone through both loops,
        # we know that the current square is
        # valid += 1

        ans += 1
        sz += 1

        # Ok so increment the value, then check to
        # see if the bottom-right most value will
        # end up in an out of bounds error.
        # Adjust based upon that.

        if row+sz > len(mat)-1 or col+sz > len(mat[0])-1:
            return ans








def countSquares(self, matrix):
    ans = 0

def itr(row, col):
    ans = 0
    sz = 0

    while True:
        # Assuming that we have valid search
        # dimensions.

        # Iterate through the bottom most
        # row, hit the 'last' element
        # Bottom search
        for i in range(col, col+sz+1):
            if matrix[row+sz][i] != 1:
                return ans

        # Iterate through the right most column
        # skip the last element
        # Far right search
        for i in range(row, row+sz):
            if matrix[i][col+sz] != 1:
                return ans

        # When have gone through both loops,
        # we know that the current square is
        # valid += 1

        ans += 1
        sz += 1

        # Ok so increment the value, then check to
        # see if the bottom-right most value will
        # end up in an out of bounds error.
        # Adjust based upon that.

        if row+sz > len(mat)-1 or col+sz > len(mat[0])-1:
            return ans


    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                ans += itr(row, col) + 1





'''

class Solution:

    def countSquares(self, matrix):
        def itr(row, col):
            ans = 0
            sz = 0

            while True:
                for i in range(col, col+sz+1):
                    if matrix[row+sz][i] != 1:
                        return ans

                for i in range(row, row+sz):
                    if matrix[i][col+sz] != 1:
                        return ans

                ans += 1
                sz += 1

                if row+sz > len(matrix)-1 or col+sz > len(matrix[0])-1:
                    return ans


        resp = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    resp += itr(row, col)

        return resp





    def countSquares_1(self, matrix):
        ans = 0
        maxSquares = min(len(matrix), len(matrix[0]))

        for i in range(1, maxSquares+1):
            # size of filter is i

            # iterate through rows
            for row in range(0, len(matrix)-i+1):

                # iterate through columns
                for col in range(0, len(matrix[0])-i+1):

                    position = matrix[row][col]

                    print("i: {} position: [{}, {}]".format(i,row, col))

                    ones = True

                    for r in range(i):
                        print(matrix[row+r][col:col+i])
                        if 0 in matrix[row+r][col:col+i]:
                            ones = False

                    if ones:
                        print("Added")
                        ans += 1

        return ans


if __name__ == '__main__':
    s = Solution()

    '''
    [1,0,1]
    [1,1,0]
    [1,1,0]

    '''

    print(s.countSquares([[1,0,1],[1,1,0],[1,1,0]]))
