'''

0123456
(()())()
      ^


stack = []

del: [4]

Things to delete:
    4 or 3
    5 or 6
    0 or 1

There is a close that is bad.
Find all consecutive closes left from position,
these all represent possibly valid closes

01
)(

stack = []

Things to delete:
    0
    1


01234567
(a)())()
     ^

stack = []

things to delete:
    5 or 4

what about

 xxx  x
()))())


When we find a close, that must be deleted
go left.

Every close we find marks a close that could also be deleted.

But then how do we not double count?

Maybe we are just getting ahead of ourselves, just count how many closes
we need to delete and how many opens we need to delete


Every close left of the closes to delete is a candidate
So:
1) Determine how many opens/closes we need to delete
2) Figure out what our options are
3) Generate all permutations of possibilities

Look to left for closes
Look to right for opens

01234567
(a)())()
       ^

stack = []

closesToDel = 5
maxClose = 5

opensToDel = 0
minOpen = float('inf')

closes_can_del = [5,4,2]

Seems like it works (for closes)

-------------------- -------------------- -------------------- --------------------

012345678
((a)(()()
        ^

stack = []
opensToDel = 2
minOpen = 0

opens_can_del = [0,1,4,5,7]

["(a)()()","(a)(())","((a))()","((a)())"]

012345678
((a)())

012345678
((a)(()()

'''

# Write function to check that everything we include is a validParen
class Solution:
    def removeInvalidParentheses(self, s):
        stack = []
        opensToDel = 0
        minOpen = float('inf')
        closesToDel = 0
        maxClose = float('-inf')

        for idx, chr in enumerate(s):
            if chr == "(":
                stack.append(idx)
            elif chr == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    closesToDel += 1
                    maxClose = idx

        # print(stack)
        while len(stack) > 0:
            opensToDel += 1
            minOpen = min(minOpen, stack.pop())

        openCandidates = []

        while minOpen < len(s):
            if s[minOpen] == "(":
                openCandidates.append(minOpen)
            minOpen += 1

        closeCandidates = []

        while maxClose >= 0:
            if s[maxClose] == ")":
                closeCandidates.append(maxClose)
            maxClose -= 1

        print(openCandidates)
        print(opensToDel)
        print(closeCandidates)
        print(closesToDel)

        validParens = set()

        # skips is a set
        def generateValid(skips, opensLeft, openList, closesLeft, closeList):
            if opensLeft == 0 and closesLeft == 0:
                validParen = ""
                for idx in range(len(s)):
                    if idx not in skips:
                        validParen += s[idx]
                validParens.add(validParen)
                return

            if opensLeft > 0:
                for idx in range(len(openList)):
                    skips.add(openList[idx])
                    generateValid(skips, opensLeft-1, openList[:idx]+openList[idx+1:], closesLeft, closeList)
                    skips.remove(openList[idx])

            if closesLeft > 0:
                for idx in range(len(closeList)):
                    skips.add(closeList[idx])
                    generateValid(skips, opensLeft, openList, closesLeft-1, closeList[:idx]+closeList[idx+1:])
                    skips.remove(closeList[idx])

        generateValid(set(), opensToDel, openCandidates, closesToDel, closeCandidates)

        return validParens




print(Solution().removeInvalidParentheses("((a)(()()"))
