'''
Given a string containing '(',')' + [a-z], remove
paren's until the string is valid. Return the string.

Minimize the # of paren's removed


 0123456789012
"lee(t(c)o)de)"
             ^

marked_idx = set({12})

stack = []

1) create set, stack
2) append/pop from stack; mark close paren's
3) mark open paren's
4) Create string based upon what is left

 01234
"))(a)(("
     ^

remove = set({0,1,4,3})
stack = []

Test cases:
- include a-z
- catch not allowed (
- catch not allowed )
- Allow legal ),(

'''

class Solution:
    def minRemoveToMakeValid(self, s):
        chrs_to_remove = set()
        stack = []

        for idx in range(len(s)):
            if s[idx] == "(":
                stack.append(idx)
            elif s[idx] == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    chrs_to_remove.add(idx)

        while len(stack) > 0:
            chrs_to_remove.add(stack.pop())

        resp = ""

        for idx in range(len(s)):
            if idx not in chrs_to_remove:
                resp += s[idx]

        return resp
