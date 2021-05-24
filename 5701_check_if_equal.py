class Solution:
    def areAlmostEqual(self, s1, s2):
        if len(s1) != len(s2): return False
        d1 = {}

        for chr in s1:
            if chr not in d1:
                d1[chr] = 1
            else:
                d1[chr] += 1

        for chr in s2:
            if chr not in d1:
                return False
            else:
                d1[chr] -= 1

        vals = list(d1.values())

        for v in vals:
            if v != 0:
                return False

        mis = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mis += 1

        if mis > 2:
            return False

        return True

s = Solution()

print(s.areAlmostEqual("bank", "kanb"))
print(s.areAlmostEqual("attack", "defend"))
print(s.areAlmostEqual("kelb", "kelb"))
print(s.areAlmostEqual("abcd", "dcba"))
