class Solution:
    def isAnagram(self, s, t):
        chrs = "abcdefghijklmnopqrstuvwxyz"

        chrCounter = {}

        for chr in chrs:
            chrCounter[chr] = 0

        for chr in s:
            chrCounter[chr] += 1

        for chr in t:
            chrCounter[chr] -= 1

        for chr in chrCounter:
            if chrCounter[chr] != 0:
                return False

        return True
