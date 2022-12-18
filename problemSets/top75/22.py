'''
Have a bfs where element is (paren, openLeft, closeLeft, count)

Where paren is the paren that is being formed, let's have it be
a string, openLeft is how many opens we can add, closeLeft is how
many closes we have left, count keeps track of whether or not we
can add a close paren.

if openLeft == 0 and closeLeft == 0:
    add resp to set

else:
    add an open if you can, add it to queue
    - If you can is determined by openLeft > 0
    add an close if you can, add it to queue
    - If you can is determined by closeLeft > 0, count > 0

create a list based upon the set, go from there
you could also have a seen composed of (paren, openLeft, closeLeft, count)
to avoid solving the same problem twice

Not sure what the time complexity/space complexity would be.

Ok so we know what the solution is, we know most of what the time complexity
is, let's do it.
'''

from collections import deque

class Solution:
    def generateParenthesis(self, n):
        q = deque([("", n,n,0)])
        ansSet = set()

        while q:
            p, pL, pR, c = q.pop()

            if pL == 0 and pR == 0:
                ansSet.add(p)
                continue

            if pL > 0:
                q.appendleft((p+"(", pL-1, pR, c+1))

            if c > 0 and pR > 0:
                q.appendleft((p+")", pL, pR-1, c-1 ))

        return list(ansSet)

print(Solution().generateParenthesis(3))
