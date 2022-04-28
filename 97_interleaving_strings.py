class Solution:
    def isInterleave(self, s1, s2, s3):
        dp = {}

        def itr(i,j,z):
            if (i,j,z) in dp:
                return dp[(i,j,z)]

            success = False

            if i >= len(s1) and j >= len(s2) and z >= len(s3):
                success = True

            elif i < len(s1) and j < len(s2) and z < len(s3):

                if s1[i] == s3[z] and s2[j] != s3[z]:
                    success = itr(i+1, j, z+1)

                elif s1[i] != s3[z] and s2[j] == s3[z]:
                    success = itr(i, j+1, z+1)

                elif s1[i] == s3[z] and s2[j] == s3[z]:
                    success = itr(i+1, j, z+1) or itr(i, j+1, z+1)

            elif i < len(s1) and z < len(s3):
                if s1[i] == s3[z]:
                    success = itr(i+1, j, z+1)

            elif j < len(s2) and z < len(s3):
                if s2[j] == s3[z]:
                    success = itr(i, j+1, z+1)

            dp[(i,j,z)] = success

            return success

        itr(0,0,0)

        return dp[(0,0,0)]


print(Solution().isInterleave("a", "b", "a"))

print(Solution().isInterleave("a", "", "c"))
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))
print(Solution().isInterleave("", "", ""))
