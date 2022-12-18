'''
Three types of brackets, determine if
string is closing. Only brackets of same
type can close each other
'''

class Solution:
    def isValid(self, s):
        bracketMap = {
        "{":"}",
        "(":")",
        "[":"]",
        }

        openSet = set({"(", "{", "["})

        stack = []

        for chr in s:
            if chr in openSet:
                stack.append(chr)
            else:
                if not stack:
                    return False

                openBracket = stack.pop()

                if bracketMap[openBracket] != chr:
                    return False

        if len(stack) != 0:
            return False

        return True

print(Solution().isValid("()"))
print(Solution().isValid("({})"))
print(Solution().isValid("({[]})"))
print(Solution().isValid("({[}])"))
print(Solution().isValid("("))
print(Solution().isValid(")"))
