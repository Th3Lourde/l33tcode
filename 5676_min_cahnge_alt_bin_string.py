class Solution:

    def minOperations(self, s):

        stringCounter1 = 0
        stringCounter2 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    stringCounter1 += 1
                else:
                    stringCounter2 += 1
            else:
                if s[i] == "1":
                    stringCounter1 += 1
                else:
                    stringCounter2 += 1

        return min(stringCounter1, stringCounter2)
