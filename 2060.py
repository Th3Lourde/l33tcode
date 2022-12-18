'''
Ok so I got some of the problem correct.

I got that we would advance with two idxs

I got that we would have four cases

I didn't get how to handle the 4th edge case,
and that we would need to use a diff

----------------------------------------------------------------------

So here is how we do it:

Our dfs has an i,j, and a diff

So we have a diff, which we add to every time we encounter a num

We only care about handling cases where one of them is an intif both of them are an int, we treat it as if it is only one

I think that the diffi s to compare the difference in length
between the two strings
if we go off of the length of the characters, I think
there is some flaw.


If diff is zero, this means that we are caught up and directly compare characters again.
else, we are in a wildcard scenario and it doesn't really matter what the value of the
characters are



'''

class Solution:
    def possiblyEquals(self, s1, s2):
        dp = {}

        def dfs(i, j, diff):
            if i == len(s1) and j == len(s2):
                return diff == 0

            if (i,j,diff) in dp:
                return dp[(i,j,diff)]

            resp = False

            if i < len(s1) and s1[i].isdigit():
                k = i
                val = 0

                while k < len(s1) and s1[k].isdigit():
                    val = val*10 + int(s1[k])
                    k += 1

                    if dfs(k, j, diff-val):
                        resp = True

            elif j < len(s2) and s2[j].isdigit():
                k = j
                val = 0

                while k < len(s2) and s2[k].isdigit():
                    val = val*10 + int(s2[k])
                    k += 1

                    if dfs(i, k, diff+val):
                        resp = True

            elif diff == 0:
                if i < len(s1) and j < len(s2) and s1[i] == s2[j] and dfs(i+1, j+1, diff):
                    resp = True

            elif diff > 0:
                if i < len(s1) and dfs(i+1, j, diff-1):
                    resp = True

            elif diff < 0:
                if j < len(s2) and dfs(i, j+1, diff+1):
                    resp = True

            dp[(i,j,diff)] = resp

            return dp[(i,j,diff)]

        dfs(0,0,0)

        return dp[(0,0,0)]

print(Solution().possiblyEquals("internationalization", "i18n"))
