class Solution:
    def removeInvalidParentheses(self, s):
        stack = []
        opens = 0
        closes = 0
        ans = set()

        for chr in s:
            if chr == "(":
                stack.append(chr)
            elif chr == ")":
                if stack:
                    stack.pop()
                else:
                    closes += 1

        opens = len(stack)

        def isValid(parenStr):
            stack = []

            for chr in parenStr:
                if chr == "(":
                    stack.append(chr)
                elif chr == ")":
                    if stack:
                        stack.pop()
                    else:
                        return False

            return len(stack) == 0

        def backtracking(idx, opens, closes, substr):
            if idx >= len(s):
                if isValid(substr):
                    ans.add(substr)
                return

            if s[idx] == "(" and opens > 0:
                backtracking(idx+1, opens-1, closes, substr)

            elif s[idx] == ")" and closes > 0:
                backtracking(idx+1, opens, closes-1, substr)

            backtracking(idx+1, opens, closes, substr+s[idx])

        backtracking(0, opens, closes, "")

        return list(ans)

print(Solution().removeInvalidParentheses("()())()"))
