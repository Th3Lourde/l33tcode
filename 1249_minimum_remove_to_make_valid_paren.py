'''
Given a string containing '(', ')', and lowercase english letters,

So we wish to identify all paren that are not valid and
remove them.

We could just record the indices that don't have a match.
Then return the string without those elements.

If "(", push. If ")", pop (if can).
Have a list of indices that we want to remove.
Do we split

2+5+2+3+10+10+6+7+8


"lee(t(c)o)de)"
 ^
s = []

"lee(t(c)o)de)"
    ^
s = ["("]




'''

class Solution:
    def minRemoveToMakeValid(self, s):
        ...
