'''
Ok so I kinda forget the trick.
I think that we are just supposed to sort
each diagonal in-place.

Yea that's try that first.

Let's do this without .sort()

loop through the different starting points,
loop through the sub-lists that we need to sort,
use binary search in order to quickly the the list

Go through the diag again, write the elements of the
list to the tmp list that we are carrying around.


1) loop through all the diags
2) loop through elements of diags, create sorted list by hand
3) loop through again, copying our sorted list to the diag
4) Profit

Start at bottom left diag

'''

class Solution:

    def diagonalSort(self, mat):

        def isValid(inp):
            if 0 <= inp[0] < len(mat) and 0 <= inp[1] < len(mat[0]):
                return True

            return False

        def appendVal(tmp, val):
            if len(tmp) == 0:
                tmp.append(val)
                return tmp

            elif tmp[0] >= val:
                tmp.insert(0, val)
                return tmp

            elif tmp[-1] <= val:
                tmp.insert(len(mat)-1, val)
                return tmp

            # Else, use binary search
            lo = 0
            hi = len(tmp)-1

            while lo < hi:
                mid = lo + int((hi-lo)/2)

                if tmp[lo] <= val <= tmp[hi] and lo+1 == hi:
                    tmp.insert(hi, val)
                    return tmp

                if tmp[mid] == val:
                    tmp.insert(mid, val)
                    return tmp

                elif tmp[mid] > val:
                    hi = mid

                else:
                    lo = mid

            if lo == hi:
                if tmp[lo] > val:
                    tmp.insert(lo, val)

                elif tmp[hi] < val:
                    tmp.insert(hi+1, val)

            return tmp

        row = [[row, 0] for row in range((len(mat)))]
        col = [[0,col] for col in range(len(mat[0]))]

        opts = row + col

        for opt in opts:
            start = opt

            tmp = []

            while isValid(start):
                # add element
                # and do other stuff
                # print(tmp)
                appendVal(tmp, mat[start[0]][start[1]])

                start[0] += 1
                start[1] += 1

            start[0], start[1] = start[0]-1, start[1]-1

            while isValid(start):
                mat[start[0]][start[1]] = tmp.pop()

                start[0] -= 1
                start[1] -= 1

        return mat




        # This works
    def diagonalSort_1(self, mat):

        def sortPos(pos):
            row = pos[0]
            col = pos[1]

            vals = []

            while row < len(mat) and col < len(mat[0]):
                vals.append(mat[row][col])
                row += 1
                col += 1

            vals.sort(reverse=True)

            row = pos[0]
            col = pos[1]

            while row < len(mat) and col < len(mat[0]):
                mat[row][col] = vals.pop()
                row += 1
                col += 1

        for i in range(len(mat[0])):
            pos = mat[0][i]
            sortPos([0,i])
            # break

        for j in range(len(mat)):
            pos = mat[j][0]
            sortPos([j,0])

        return mat




if __name__ == '__main__':
    s = Solution()
    s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])

    # print(s.diagonalSort([["a","b","c","d"],["e","f","g","h"],["i","j","k","l"]]))

    s.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]])

    print_matrix([[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]])
