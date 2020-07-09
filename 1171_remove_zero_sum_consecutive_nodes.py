'''
start cooking soon


Ok so I'm pretty sure that we should be
using a stack.

see value, check to see if we pop we get zero.
If yes, remove all values that allow us to do this.

Right now, my solution might be 0(n^2). No. 2n worst case.
Once we look through all of the elements, we remove them
from the stack.

If no, push value to stack

e.g.

[1,2,-3,3,1]

s = []

[1,2,-3,3,1]
 ^
s = []
v = 1

s = [1]
v = 1

[1,2,-3,3,1]
      ^
s = [1,2]
v = 2

[1,2,-3,3,1]
      ^
s = [1,2]
v = -3

del [1,2] -3

s = []
val = -3
[1,2,-3,3,1]
        ^
s = [3]
val = 3

[1,2,-3,3,1]
          ^
s = [3, 1]
val = 1

start at lhs of stack, create new
linked list.

Checking all of the elements is the tricky
part. We could have another stack that represents
the number of negative numbers in the stack.

e.g.
neg = [0,0, 1,1,1, 2,2]
s   = [0,1,-2,4,5,-2,1]

Why would this be helpful?
well if our sum is positive and we hit
and index where neg[index] == 0, we know that
we can stop. Prevents us from always looking at
all of the elements

So how do we do the check? have index i, decrement
it

If we get pos/neg numbers as similar frequency, we
would probably have some nested logic to know when
we are done. Ignore this for now.

neg = []int
s = []int

i = len(s)-1

val = ll[z]

cons = False

while stack and i >= 0:
    if val + s[i:] == 0:
        s = s[:i]
        cons = True
        break

    i -= 1

if not cons:
    s.append(val)

we obv don't want 0 to be in our list.

Ok so this is slow as balls. Read how to make
it faster, add to optimize, move on.

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeZeroSumSublists(self, head):
        s = []
        node = head

        # 1) Remove zeroSum elements

        while node:
            i = len(s)-1
            cons = False

            while s and i >= 0:
                if node.val + sum(s[i:]) == 0:
                    s = s[:i]
                    cons = True
                    break
                i -= 1

            if not cons and node.val != 0:
                s.append(node.val)
            node = node.next

        # 2) Create answer from what is left.

        if not s: return None

        head = ListNode(s[0])
        node = head

        for i in range(1, len(s)):
            node.next = ListNode(s[i])
            node = node.next

        return head
