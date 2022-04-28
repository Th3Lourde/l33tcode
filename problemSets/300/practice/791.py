class Solution:
    def customSortString(self, order, s):
        s_set = {}
        ans = []

        for idx, chr in enumerate(s):
            if chr in s_set:
                s_set[chr] += 1
            else:
                s_set[chr] = 1

        for chr in order:
            if chr in s_set:
                while s_set[chr] > 0:
                    ans.append(chr)
                    s_set[chr] -= 1

                del s_set[chr]

        for chr in s_set:
            while s_set[chr] > 0:
                ans.append(chr)
                s_set[chr] -= 1

        return "".join(ans)


print(Solution().customSortString("cbafg", "aabcdddd"))
print(Solution().customSortString("cba", "abcd"))
