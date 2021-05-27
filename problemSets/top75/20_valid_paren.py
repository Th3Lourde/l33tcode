class Solution:
    def isValid(self, s):
        stack = []

        mapping = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        for chr in s:
            if chr in set({"(", "{", "["}):
                stack.append(chr)
                continue

            if not stack:
                return False

            if stack.pop() != mapping[chr]:
                return False

        return len(stack) == 0


print(Solution().isValid("()")) # True
print(Solution().isValid("()[]{}")) # True
print(Solution().isValid("(]")) # False
print(Solution().isValid("([)]")) # False
print(Solution().isValid("{[]}")) # True
print(Solution().isValid("{[")) # False
print(Solution().isValid("{[])}")) # False
