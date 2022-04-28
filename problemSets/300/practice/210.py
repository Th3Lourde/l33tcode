class Solution:
    def findOrder(self, numCourses, prerequisites):
        course_to_prereq = {}

        for course in range(numCourses):
            course_to_prereq[course] = set()

        for course, prereq in prerequisites:
            course_to_prereq[course].add(prereq)

        courses_to_take = set()

        for course in range(numCourses):
            courses_to_take.add(course)

        taken = set()
        resp = []
        progress = True

        while progress:
            progress = False
            courses_taken = set()

            for course in courses_to_take:
                if course not in taken and len(course_to_prereq[course] - taken) == 0:
                    progress = True
                    courses_taken.add(course)
                    taken.add(course)
                    resp.append(course)

            courses_taken -= courses_taken

        if len(resp) == numCourses:
            return resp

        return []

print(Solution().findOrder(1, []))

print(Solution().findOrder(2, [[1,0]]))
print(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
