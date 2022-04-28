'''
You are given an array of non overlapping intervals

Insert the new interval into intervals in such a way
that the intervals are still in sorted order and
they cannot be merged any further.

[1,2],[3,5],[6,7],[8,10],[12,16]
         ^
newInterval = [4,8]

When inserting:
Check that newInterval[0] < intervals[i][1]

Find a term to start at.

Term to start at has the characteristic that:
intervals[i][0] <= newInterval[0] <= intervals[i][1]

Next we find a term to end at.

The term to end at as the following characteristic:
intervals[i][0] <= newInterval[1] <= intervals[i][1]

Find the term that meets that characteristic (if one exists)
update the right accordingly, add it to the new list.

We are either inserting at the front
at the end
middle with merge
middle without merge
'''

class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]

        # See if we can insert at LHS
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        # See if we can insert at RHS
        if intervals[len(intervals)-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals

        # We need to merge
        l = newInterval[0]
        r = newInterval[1]

        # Find if there's a better L value
        for i in range(len(intervals)):
            if intervals[i][0] <= l <= intervals[i][1]:
                l = intervals[i][0]
            if intervals[i][0] <= r <= intervals[i][1]:
                r = intervals[i][1]

        # print("L: {}".format(l))
        # print("R: {}".format(r))
        # Figure out when to insert [L,R]
        insertedArr = []
        inserted = False

        for i in range(len(intervals)):
            if inserted == False and (l <= r <= intervals[i][0]):
                insertedArr.append([l,r])

                if not(l <= intervals[i][0] <= intervals[i][1] <= r):
                    insertedArr.append(intervals[i])

                inserted = True
            elif l <= intervals[i][0] <= intervals[i][1] <= r:
                continue
            else:
                insertedArr.append(intervals[i])

        if inserted == False:
            insertedArr.append([l,r])

        if len(insertedArr) == 0:
            insertedArr.append([l,r])

        return insertedArr


print(Solution().insert([[3,4],[6,6],[7,10],[13,13],[17,17],[26,29],[35,38],[43,49]], [13,17]))

print(Solution().insert([[0,2],[3,9]],[0,1]))

print(Solution().insert([[0,2],[3,9]],[6,8]))

print(Solution().insert([[2,3]], [1,5]))
print(Solution().insert([[1,5]], [2,3]))
print(Solution().insert([[1,2],[6,7],[8,10],[12,16]], [17,19]))
print(Solution().insert([[1,2],[6,7],[8,10],[12,16]], [1,7]))
print(Solution().insert([[1,2],[6,7],[8,10],[12,16]], [3,5]))
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [-2,0]))
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [18,20]))
