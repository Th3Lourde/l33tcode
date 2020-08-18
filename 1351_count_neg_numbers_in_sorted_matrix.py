'''
[
    [ 4, 3, 2,-1],
    [ 3, 2, 1,-1],
    [ 1, 1,-1,-2],
    [-1,-1,-2,-3]
]

Given a matrix that is sorted in a certain way,
return the number of negative numbers in the matrix.

Start from bottom right and move up.
If the initial value is not negative, then there are
no more negative values left.

Also, if a positive number occurs in either of the future
scans of a row/column, then there is not a negative number
left in the matrix.

So start at bottom right, have a boolean val for if we should
continue or not.

if bool == True, adjust the starting point, else stop.

Have an outer function that updates the starting if prev
starting returned true.

Have inner that counts num of negative values and returns
t/f if any non neg values were observed.

So instead of noting if we see a pos, note if we see a neg?

# Starting Point
sP = [row column]
sP = [len(m), len(m[0])]

ans = 0

while sP != [0, 0]:
    negObserved, shouldContinue = itr(sP)
    ans += negObserved

    if shouldContinue:
        sP[0] -= 1
        sP[1] -= 1

return ans

[
    [ 3, 2],
    [-3,-3],
    [-3,-3],
    [-3,-3]
]



'''

class Solution:

    def countNegatives(self, m):
        ans = 0
        sP = [len(m)-1, len(m[0])-1]

        def itr(sP):
            foundNeg = False
            neg = 0

                # Row First
            for i in range(sP[0], -1, -1):
                if m[i][sP[1]] < 0:
                    neg += 1

                    if foundNeg == False:
                        foundNeg = True


                # Column Second
            for i in range(sP[1]-1, -1, -1):
                if m[sP[0]][i] < 0:
                    neg += 1

                    if foundNeg == False:
                        foundNeg = True


            return neg, foundNeg

            # sP == Starting Point
        while sP[0] >= 0 and sP[1] >= 0:
            negObserved, foundNeg = itr(sP)
            ans += negObserved

            if foundNeg:
                sP[0] -= 1
                sP[1] -= 1

            else:
                break

        return ans

    def countNegatives_1(self, m):
        ans = 0
        sP = [len(m)-1, len(m[0])-1]

        def itr(sP):
            foundPos = False
            neg = 0

                # Row First
            for i in range(sP[0], -1, -1):
                if m[i][sP[1]] < 0:
                    neg += 1
                else:
                    foundPos = True
                    break

                # Column Second
            for i in range(sP[1]-1, -1, -1):
                if m[sP[0]][i] < 0:
                    neg += 1
                else:
                    foundPos = True
                    break

            return neg, foundPos

            # sP == Starting Point
        while sP != [-1, -1]:
            negObserved, foundPos = itr(sP)
            ans += negObserved

            if foundPos == False:
                sP[0] -= 1
                sP[1] -= 1

            else:
                break

        return ans
