class Solution:
    def isAnagram(self, s, t):
        chrMapS = {}
        chrsLeft = 0

        for chr in s:
            if chr not in chrMapS:
                chrMapS[chr] = 1
            else:
                chrMapS[chr] += 1

            chrsLeft += 1

        for chr in t:
            if chr not in chrMapS:
                return False

            chrMapS[chr] -= 1
            chrsLeft -= 1

            if chrMapS[chr] < 0:
                return False

        return chrsLeft == 0


print(Solution().isAnagram("abbc", "cba"))
print(Solution().isAnagram("abc", "cba"))
print(Solution().isAnagram("abc", "cb"))
print(Solution().isAnagram("a", "a"))
