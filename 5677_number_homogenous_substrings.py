'''
abbcccaa
     i
        j

run = 2
ans = 1

'''

class Solution:
    def countHomogenous(self, s):
        ans = 0
        i = 0

        while i < len(s):
            # Find repeats
            j = i
            run = 0

            while j < len(s) and s[i] == s[j]:
                run += 1
                j += 1

            ans += int(run*(run+1)/2)

            i = j

            # Return with the proper mod
        return ans
