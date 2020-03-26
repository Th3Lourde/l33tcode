

'''
Given s,t what is the minimum number
of characters in s must you replace s.t.
it is an anagram of t (has same number of

1) Create dict of both
2) Count characters in t missing from s
3) Count characters in s that you can delete (equal sizes, forget it)

So if d[t] - d[s] > 0, add diff to answer


'''

class Solution:
    def minSteps(self, s, t):
        ds = {}
        dt = {}

        for i in range(len(s)):
            try:
                ds[s[i]] += 1
            except:
                ds[s[i]] = 1

            try:
                dt[t[i]] += 1
            except:
                dt[t[i]] = 1


        ans = 0

        for key in dt:
            try:
                if dt[key] - ds[key] > 0:
                    ans += dt[key] - ds[key]

            except:
                ans += dt[key]


        return ans


if __name__ == '__main__':
    s = Solution()


    print(s.minSteps(s = "bab", t = "aba"))
    print(s.minSteps(s = "leetcode", t = "practice"))
    print(s.minSteps("anagram", t = "mangaar"))
    print(s.minSteps("xxyyzz", t = "xxyyzz"))
    print(s.minSteps(s = "friend", t = "family"))
