'''
s = "codeleet",
indices = [4,5,6,7,0,2,1,3]

 45670213
"codeleet"
        ^

num_to_chr = {4:c, 5:o, 6:d, 7:e, 0:l, 2:e, 1:e, 3:t}


'''


class Solution:
    def restoreString(self, s, indices):
        num_to_chr = {}

        for idx in range(len(s)):
            num_to_chr[indices[idx]] = s[idx]

        resp = ""

        for idx in range(len(s)):
            resp += num_to_chr[idx]

        return resp

print(Solution().restoreString("codeleet", [4,5,6,7,0,2,1,3]))
print(Solution().restoreString("", []))
