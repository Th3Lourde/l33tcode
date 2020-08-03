'''
Fuck this problem so hard.
So literally just sort each diag in place

So loop through the different start points
for the diags, get all the elements, sort them,
then move on to the next point.
'''

class Solution:
    def diagonalSort(self, mat):

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

def print_matrix(m):
    for r in m:
        print(r)

# print_matrix([[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]])

if __name__ == '__main__':
    s = Solution()
    # print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
    # print(s.diagonalSort([["a","b","c","d"],["e","f","g","h"],["i","j","k","l"]]))

    s.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]])

    print_matrix([[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]])
