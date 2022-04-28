'''
Given two lists of lists.
Each list contains intervals.
Intervals are sorted in both lists.
Return the intersection of these two interval lists.

So we'll have two indices, move the one that is attached to the smaller
max.

have a var called left bound.
If left bound exists, we are looking for the right bound
If left bound dne, we are looking for the left bound (maybe right)
And there is a special case when we are dealing with the last element

Since they are disjoint, we only need to worry about finding the intersection
between any two idxs.

So the question is really which idx do we increment, the one with the lower max

'''

class Solution:
    def intervalIntersection(self, firstList, secondList):
        intersections = []
        idx1 = 0
        idx2 = 0

        while idx1 < len(firstList) and idx2 < len(secondList):

            # Record the intersection (if exists)
            if firstList[idx1][0] <= secondList[idx2][0] <= firstList[idx1][1]  <= secondList[idx2][1]:
                # |   |
                #   |   |
                intersections.append([secondList[idx2][0], firstList[idx1][1]])
            elif secondList[idx2][0] <= firstList[idx1][0] <= secondList[idx2][1] <= firstList[idx1][1]:
                #   |   |
                # |   |
                intersections.append([firstList[idx1][0], secondList[idx2][1]])

            elif secondList[idx2][0] <= firstList[idx1][0] <= firstList[idx1][1] <= secondList[idx2][1]:
                #  |   |
                # |     |
                intersections.append(firstList[idx1])

            elif firstList[idx1][0] <= secondList[idx2][0] <= secondList[idx2][1] <= firstList[idx1][1]:
                #  | |
                # |   |
                intersections.append(secondList[idx2])

            if firstList[idx1][1] <= secondList[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1

        return intersections
