class Solution:
    def myAtoi(self, s):
        isNeg = False
        numStart = False
        n = len(s)
        i = 0
        num = ['0']
        nums = set({'0','1','2','3','4','5','6','7','8','9'})
        signs = set({'+', '-'})

        while i < n:
            if not numStart and s[i] == " ":
                i += 1
                continue

            elif numStart and s[i] not in nums:
                break

            elif s[i] not in signs.union(nums):
                break

            elif not numStart and s[i] in signs:
                numStart = True
                if s[i] == '-':
                    isNeg = True

            elif not numStart and s[i] in nums:
                numStart = True
                num.append(s[i])

            elif s[i] in nums:
                num.append(s[i])

            i += 1

        resp = int("".join(num))

        if isNeg:
            resp *= -1

        if resp < -2**31:
            return -2**31

        elif resp > 2**31-1:
            return 2**31-1

        return resp



print(Solution().myAtoi("42"))
print(Solution().myAtoi("-42"))
print(Solution().myAtoi("   -42"))
print(Solution().myAtoi("-   -42"))
print(Solution().myAtoi("- -1   -42"))
print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("-91283472332"))
