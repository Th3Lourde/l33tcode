'''
Given two strings:
- start
- target

len(start) == len(target)

both strings consist of 'L', 'R', '_'

We can move some of the characters in the string
- can move L
- can move R

Can move L
- only to the left
- iff there is a blank space to the left

Can move R
- only to the right
- iff there is a blank space to the right

return t/f if you can move the contents of start,
according to the rules, such that target is your
final result.

I believe the answer is always true as long as
we are not required for L and R to switch places.

and if the target position does not require an R
to move to the left and an L to the right.

two pointer approach, for every non-space element,
can we get the proper character from start to move
to target.

When finding targets for R:
- can only move left, if we find an L first, return false

When finding target for L:
- can only move right, if we find an R first, return false

have a set with elements you have successfully moved.
it shouldn't matter if we deal with the left side of the
string before dealing with the right side.

Loop through target.
If L, look right to see if there is an L
If R, look right to see if there is an R


X_____X
_____RR
      ^

X_X___X_
_R___R_R
       ^


So it looks like this works, it is slow, at 0(n^2)
We can speed it up to nlog(n) by using heaps for l,r

We want the smallest R's (r can only look left)
We want the largest L's (l can only look right)

012345
L_L___
LL____
^

[0]
'''

import heapq

class Solution:
    def canChange(self, start, target):
        startList = []
        targList = []
        visited = set()
        n = len(start)

        for chr in start:
            if chr != "_":
                startList.append(chr)

        for chr in target:
            if chr != "_":
                targList.append(chr)

        aStr = "".join(startList)
        bStr = "".join(targList)

        if aStr != bStr:
            return False

        if "_" not in start:
            return start == target

        lHeap = []
        rHeap = []

        for idx, chr in enumerate(start):
            if chr == "R":
                heapq.heappush(rHeap, idx)
            elif chr == "L":
                heapq.heappush(lHeap, idx)

        for idx in range(len(target)):
            if target[idx] == "L":
                if not lHeap:
                    return False

                maxL = heapq.heappop(lHeap)

                if maxL < idx:
                    return False

            elif target[idx] == "R":
                if not rHeap:
                    return False

                minR = heapq.heappop(rHeap)

                if minR > idx:
                    return False

        return True



print(Solution().canChange("L_L___", "LL____"))
