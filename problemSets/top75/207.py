'''
There are a total of numCourses
and there is a dependency map of courses you must take
before you can take a course.

Given the dependency map, return t/f if you can take all
of the courses

prerequisites[i] = [a,b]

where you take b if you want to take a

So step one is to build up out pre-req graph.

Where key is the course, value are the courses we need to take
We can also have a set of courses we have taken.

1) Populate the map
2) Then check to see what courses don't have pre-req, take those
courses.
3) Loop through map, if we have enough courses to take a class, take it
4) Continue this way until we are not able to take any more courses
5) Return numCourses = len(taken)

'''

class Solution:
    def canFinish(self, numCourses, prerequisites):
        taken = set()
        map = {}

        for req, c in prerequisites:
            if c in map:
                map[c].add(req)
            else:
                map[c] = set({req})


        for c in range(numCourses):
            if c not in map:
                taken.add(c)


        tookClass = True

        while tookClass:
            tookClass = False

            for course in map:
                if course not in taken:
                    if map[course]-taken == set():
                        taken.add(course)
                        tookClass = True

        return len(taken) == numCourses
