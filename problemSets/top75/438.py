class Solution:
    def findAnagrams(self, s, p):
        target = {}
        tmp = {}
        ans = []
        n = len(s)
        targetCount = len(p)


        for chr in p:
            if chr in target:
                target[chr] += 1
            else:
                target[chr] = 1

        # print(target)

        l = 0
        r = 0

        while r < n:
            if target == tmp:
                ans.append(l)

            if s[r] in target:
                while r < n and s[r] in target and (r-l+1) <= targetCount:
                    if s[r] in tmp:
                        tmp[s[r]] += 1
                    else:
                        tmp[s[r]] = 1
                    r += 1

                if target == tmp:
                    ans.append(l)

                # Delete left most element
                tmp[s[l]] -= 1
                if tmp[s[l]] == 0:
                    del tmp[s[l]]
                l += 1

                # Then keep deleting until we are at an element
                # That is in target
                while l < r and s[l] not in target :
                    tmp[s[l]] -= 1
                    if tmp[s[l]] == 0:
                        del tmp[s[l]]
                    l += 1

                if target == tmp:
                    ans.append(l)

            else:
                l = r+1
                r = r+1
                tmp = {}

        return ans

print(Solution().findAnagrams("cbaebabacd", "abc"))

'''
cbaebabacd
l
  r

target = {
a:1,
b:1,
c:1
}

tmp = {
c : 1
b : 1
}
'''
