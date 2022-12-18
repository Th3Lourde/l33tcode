class Solution:
    def canConstruct(self, ransomNote, magazine):
        d = {}

        for chr in magazine:
            if chr in d:
                d[chr] += 1
            else:
                d[chr] = 1

        for chr in ransomNote:
            if chr in d:
                if d[chr] > 0:
                    d[chr] -= 1

                else:
                    return False

            else:
                return False

        return True
