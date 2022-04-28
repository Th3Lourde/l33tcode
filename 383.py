class Solution:
    def canConstruct(self, ransomNote, magazine):
        dict = {}

        for chr in magazine:
            if chr not in dict:
                dict[chr] = 1
            else:
                dict[chr] += 1

        for chr in ransomNote:
            if chr not in dict:
                return False
            else:
                dict[chr] -= 1

            if dict[chr] < 0:
                return False

        return True

print(Solution().canConstruct("a", "b"))
print(Solution().canConstruct("aa", "ab"))
print(Solution().canConstruct("aa", "aba"))
print(Solution().canConstruct("aa", "aab"))
