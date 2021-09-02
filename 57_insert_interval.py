class Solution:
    def insert(self, intervals, newInterval):
        termToAdd = newInterval

        if len(intervals) == 0:
            return [newInterval]

        for l,r in intervals:
            if newInterval[0] <= r:
                termToAdd[0] = min(termToAdd[0], l)
                break

        for l,r in intervals:
            if l <= newInterval[1] <= r:
                termToAdd[1] = max(termToAdd[1], r)
                break

        haveNotAdded = True
        insertedList = []

        for l,r in intervals:
            if r < termToAdd[0]:
                insertedList.append([l,r])

            elif termToAdd[1] < l:

                if haveNotAdded:
                    insertedList.append(termToAdd)
                    haveNotAdded = False

                insertedList.append([l,r])

        if haveNotAdded:
            insertedList.append(termToAdd)
            haveNotAdded = False

        return insertedList


print(Solution().insert([[1,5]], [0,8]))


print(Solution().insert([[1,3],[6,9]], [2,5]))
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(Solution().insert([], [5,7]))
print(Solution().insert([[1,5]], [2,3]))
print(Solution().insert([[1,5]], [2,7]))
