class Solution:
    def findOrder(self, numCourses, prerequisites):
        ans = []
        ansSet = set()
        coursesLeft = set()
        courseToPreReq = {}

        for course in range(numCourses):
            courseToPreReq[course] = set()
            coursesLeft.add(course)

        for course, preReq in prerequisites:
            courseToPreReq[course].add(preReq)

        # initial pass, take all courses that have no pre-req
        for course in range(numCourses):
            if len(courseToPreReq[course]) == 0:
                ans.append(course)
                ansSet.add(course)
                coursesLeft.remove(course)

        # print(ans)
        # print(ansSet)
        # print(courseToPreReq)

        advanced = True

        while advanced:
            advanced = False

            # print(ansSet)

            for courseLeft in coursesLeft:
                # print(courseLeft)
                # print(courseToPreReq[courseLeft])
                # print(ansSet)

                if courseToPreReq[courseLeft] - ansSet == set():
                    # print("!")
                    advanced = True
                    ans.append(courseLeft)
                    ansSet.add(courseLeft)

            coursesLeft = coursesLeft - ansSet

            if coursesLeft == set():
                return ans

        return []

print(Solution().findOrder(3, [[0,1],[0,2],[1,2]]))
print(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(2,[[1,0]]))
print(Solution().findOrder(3,[[1,0]]))
