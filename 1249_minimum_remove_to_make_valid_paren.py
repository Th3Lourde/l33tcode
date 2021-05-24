class Solution:
    def minRemoveToMakeValid_1(self, s):
        rm = set()
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            elif s[i] == ")":
                if stack:
                    stack.pop()

                elif not stack:
                    rm.add(i)

        for i in range(len(stack)):
            rm.add(stack[i])

        ans_s = ""

        for i in range(len(s)):
            if i not in rm:
                ans_s = ans_s + s[i]

        return ans_s

    def minRemoveToMakeValid_2(self, s):
        skip = set()
        count = 0

        for idx in range(len(s)):
            chr = s[idx]

            if chr == ")":
                if count < 1:
                    skip.add(idx)
                else:
                    count -= 1
            elif chr == "(":
                count += 1

        idx = len(s)-1
        while count > 0:
            if s[idx] == "(":
                skip.add(idx)
                count -= 1
            idx -= 1

        ans = ""

        for idx in range(len(s)):
            if idx not in skip:
                ans += s[idx]

        return ans

    def minRemoveToMakeValid(self, s):
        remove = set()
        open = []

        for idx, chr in enumerate(s):
            if chr == "(":
                open.append(idx)
            elif chr == ")":
                if open:
                    open.pop()
                else:
                    remove.add(idx)

        for idx in open:
            remove.add(idx)

        valid = ""

        for idx, chr in enumerate(s):
            if idx not in remove:
                valid += chr

        return valid

if __name__ == '__main__':
    s = Solution()
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(s.minRemoveToMakeValid("))(("))
    print(s.minRemoveToMakeValid("(a(b(c)d)"))
