'''
"ay"
  ^

have a pointer
look to  see if the element on the right is adjacent
if is is remove the element and the element on the right
idx -=1
idx = max(0, idx-1)

else idx +=1
'''

class Solution:
    def removeDuplicates(self, s):
        idx = 0

        while idx < len(s)-1:
            if s[idx] == s[idx+1]:
                s = s[:idx] + s[idx+2:]
                idx = max(0, idx-1)

            else:
                idx += 1

        return s

print(Solution().removeDuplicates("zazzaxyww"))
print(Solution().removeDuplicates("azxxzy"))
