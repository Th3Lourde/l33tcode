'''
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The string is valid if the parentheses can
close correctly.

If we see a close, pop from the stack,
the element on the top of the stack should be
the corresponding open. If it isn't, return False

If we see an open, add to stack

After all elements have been see, return len(stack) == 0
'''

class Solution:
    def isValid(self, s):
        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for chr in s:
            if chr in set({"{", "(", "["}):
                stack.append(chr)
            else:
                if len(stack) == 0 or stack[-1] != closeToOpen[chr]:
                    return False

                stack.pop()

        return len(stack) == 0

print(Solution().isValid("()")) # True
print(Solution().isValid("()[]{}")) # True
print(Solution().isValid("(]")) # False
print(Solution().isValid("([)]")) # False
print(Solution().isValid("{[]}")) # True
print(Solution().isValid("")) # True
print(Solution().isValid("]")) # False
print(Solution().isValid("[")) # False
