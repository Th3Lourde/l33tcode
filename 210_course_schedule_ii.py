class Solution:
    def findOrder(self, numCourses, prerequisites):
        taken = set()
        courses = []
        hasCycle = [False]

        preReqDict = {i:set() for i in range(numCourses)}

        for p in prerequisites:
            preReqDict[p[0]].add(p[1])

        def itr(n, cycleDetector, hasCycle):
            if n in cycleDetector:
                hasCycle[0] = True
                return
            cycleDetector.add(n)

            if n in preReqDict:
                for pre in preReqDict[n]:
                    if pre not in taken:
                        if pre in cycleDetector:
                            hasCycle[0] = True
                            return
                        itr(pre, cycleDetector, hasCycle)

            taken.add(n)
            courses.append(n)

        for i in range(numCourses):
            if i not in taken:
                itr(i, set(), hasCycle)

        if hasCycle[0] == True: return []

        return courses

if __name__ == '__main__':
    s = Solution()

    print(s.findOrder(3, [[0,1],[0,2],[1,2]]))
    print(s.findOrder(4,[[1,0],[2,0],[3,1],[3,2]] ))
    print(s.findOrder(3, [[1,0],[0,2],[2,1]]))
