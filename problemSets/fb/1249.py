'''
Given a string of '(' ')' and lowercase English characters

Remove the minimum number of parentheses so that the resulting
string is valid.

Return the resulting string

So write an algo that tracks whether or not

Let's keep track of the idx of all paren we want to del.

Once we have the list, go through one last time and create the
string that we are going to return.

Also have one list for open, another for close. Store the idx of the
open/close paren

0123456789012
lee(t(c)o)de)
            ^

del = [12]
open = []
close = []

1234567
a)b(c)d
     ^

del = set(2)
open = []
close = []



'''

class Solution:
    def minRemoveToMakeValid(self, s):
        chrsToDel = set()
        open = []

        for idx in range(len(s)):
            if s[idx] == "(":
                open.append(idx)

            elif s[idx] == ")":
                if len(open) == 0:
                    chrsToDel.add(idx)
                else:
                    open.pop()

        while open:
            chrsToDel.add(open.pop())

        returnStr = ""

        for idx in range(len(s)):
            if idx not in chrsToDel:
                returnStr += s[idx]

        return returnStr


print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
print(Solution().minRemoveToMakeValid("a)b(c)d"))
print(Solution().minRemoveToMakeValid("))(("))
print(Solution().minRemoveToMakeValid("(a(b(c)d)"))
