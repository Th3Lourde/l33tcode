class Solution:
    def minWindow(self, s, t):
        ans = ""
        goal = {}

        for chr in t:
            if chr not in goal:
                goal[chr] = 1
            else:
                goal[chr] += 1

        l = 0
        r = 0

        def validSubStr(dict):
            for key in goal:
                if key not in dict or goal[key] > dict[key]:
                    return False
            return True

        current = {}

        while r < len(s):
            # print("Substr: {}, current: {}".format(s[l:r+1], current))

            if s[r] not in current:
                current[s[r]] = 1
            else:
                current[s[r]] += 1


            while validSubStr(current):
                if len(ans) == 0 or len(ans) > len(s[l:r+1]):
                    ans = s[l:r+1]

                current[s[l]] -= 1
                l += 1

            r += 1

        return ans


print(Solution().minWindow("ab", "a"))
# print(Solution().minWindow("ADOBECODEBANC", "ABC"))
