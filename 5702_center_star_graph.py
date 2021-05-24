class Solution:
    def findCenter(self, edges):
        s1 = set({edges[0][0], edges[0][1]})
        s2 = set({edges[1][0], edges[1][1]})

        center = s1.intersection(s2)

        t = list(center)
        return t[0]


s = Solution()

print(s.findCenter([[1,2],[2,3],[4,2]]))
