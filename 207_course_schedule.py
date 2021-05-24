
class Solution:
    def canFinish(self, numCourses, prerequisites):
        classesTaken = set()
        preReqsForClass = {}
        keys = set()

        for n in range(numCourses):
            preReqsForClass[n] = set()
            keys.add(n)

        for l,r in prerequisites:
            preReqsForClass[l].add(r)

        # print(preReqsForClass)
        tookNewClass = True

        while tookNewClass:
            tookNewClass = False

            for c in keys:
                if c in classesTaken:
                    continue

                if preReqsForClass[c] == set() or preReqsForClass[c] - classesTaken == set():
                    classesTaken.add(c)
                    tookNewClass = True

            keys -= classesTaken


        return len(classesTaken) == numCourses

print(Solution().canFinish(3, [[1,0],[1,2],[0,1]]))
