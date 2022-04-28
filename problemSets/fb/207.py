'''
There are a total of num courses that you need to take.
Each course is labeled from 0 to numCourses-1

You are given an array where:
array[i] = [courseA, courseB]

Where courseB is a preReq for courseA

Return true or false if you can take all of the courses

Let's make a map[string] --> set

Let's also have a set of courses that we have taken.

Loop through dict, if prereqs-takes != empty, we can't take
the course.

Else we can take the course

Have a bool that marks whether or not we were able to take
a new course.

So how would we go about doing this?
DFS on a node would just be looking for cycles

4 --> [3,2,1]
Can we take 3 without encountering a cycle?
Can we take 2 without encountering a cycle?
Can we take 1 without encountering a cycle?


'''


class Solution:
    def canFinish_1(self, numCourses, prerequisites):
        taken = set()

        prereqDict = {}

        for course in range(numCourses):
            prereqDict[course] = set()

        for course, preq in prerequisites:
            prereqDict[course].add(preq)

        takenCourse = True

        while takenCourse:
            takenCourse = False

            for course in prereqDict:
                if course in taken:
                    continue
                elif prereqDict[course]-taken == set():
                    # We have all of the pre-reqs
                    takenCourse = True
                    taken.add(course)

        return len(taken) == numCourses

    def canFinish(self, numCourses, prerequisites):
        taken = set()

        prereqDict = {}

        for course in range(numCourses):
            prereqDict[course] = set()

        for course, preq in prerequisites:
            prereqDict[course].add(preq)

        def dfs(course, seen):
            if course in taken:
                return True

            canComplete = True

            for preReq in prereqDict[course]:
                if preReq in seen:
                    return False

                seen.add(preReq)

                if not dfs(preReq, seen):
                    canComplete = False
                    break

                seen.remove(preReq)

            if canComplete == False:
                return False

            taken.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True


print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(3, [[1,0], [2,1], [2,0]]))
print(Solution().canFinish(2, [[1,0],[0,1]]))
