'''
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

Given two lists, which are composed of subLists,
which represent intervals (which are all sorted),
return all intersections

Ok so let's have interval A and interval B.

Ok so it can't actually span multiple

We can calculate the intersection by looking at the bounds


have an idx for firstList and secondList

Calculate the interval of intersection (if one exists)
Then get the next interval for the interval with the smallest
upper bound.

If we can't get the next interal, return intersections

how to tell if there is an intersection?
[[4,6],[7,8],[10,17]]
        ^

[[5,10]]
  ^

'''

class Solution:
    def intervalIntersection(self, firstList, secondList):
        idx1 = 0
        idx2 = 0
        intersections = []

        while idx1 < len(firstList) and idx2 < len(secondList):
            if firstList[idx1][0] <= secondList[idx2][0] <= firstList[idx1][1]:
                intersections.append([secondList[idx2][0], min(secondList[idx2][1], firstList[idx1][1])])


            elif firstList[idx1][0] <= secondList[idx2][1] <= firstList[idx1][1]:
                intersections.append([max(firstList[idx1][0], secondList[idx2][0]), secondList[idx2][1]])

            elif firstList[idx1][0] <= secondList[idx2][0] <= secondList[idx2][1] <= firstList[idx1][1]:
                intersections.append(secondList[idx2])

            elif secondList[idx2][0] <= firstList[idx1][0] <= firstList[idx1][1] <= secondList[idx2][1]:
                intersections.append(firstList[idx1])

            if firstList[idx1][1] < secondList[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
            # print("idx1: {} | idx2: {} | intersections: {}".format(idx1, idx2, intersections))


        return intersections

print(Solution().intervalIntersection([[4,6],[7,8],[10,17]], [[5,10]]))

print(Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
