'''
Given head.
Return an array of integers arr, where arr[i]
is the value of the closest node that is greater than i.

2 --> 1 --> 5
[5,5,0]

Ok so I feel a stack coming on.

2 --> 1 --> 5
^

[]
see 2, add it to stack
[2]

2 --> 1 --> 5
      ^
see 1, peek stack, if bigger,
pop from stack and add node.val for ans[i]
not the case, push 1 to stack.

[2,1]
2 --> 1 --> 5
            ^
5.val > s.peek():
    while we want to, pop and do the thing.

Buuttt what if node.val < stack.peek
and ∃ node ∈ stack ∋ that node < node.val?

Then we would have:
[a,b], c

where c < b, a < c.
If this was true, then b would have picked up the slack.


we need a way to get the indeces for ans.
I think storing elements with indices would help. But do we
need to?

[2,4,7,4,3,5]
 ^
s = []

s = [2]
ans = [1]
[5,4,7,4,3,5]
   ^
s = [4]

Yes we do.

How large do we make our list? Can we just use .insert()?
No, cause .insert() will just append if size is too big.

Solution? Can we hash list nodes? Yes.

Ok. Pass 1:

loop through linked list, use stack, add values to dict,
d[node]: val

second loop through linked list, append to ans.

A better way to do it?
Not unless we use some dynamic list stuff.

0(2n) = 0(n)
0(2n) = 0(n)

Ok so the hashing isn't working.
Maybe we instead create a dict [int] --> int
where it is index --> ans[i]

'''
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

    def __str__(self):
        return "{}{}".format(self.val, self.next)

class Solution:

    def nextLargerNodes(self, head): # Also works, sick.
        if not head: return []

        ans = []
        stack = deque()
        node = head
        i = 0

        while node:
            while stack and stack[-1][0] < node.val:
                val, idx = stack.pop()
                ans[idx] = node.val

            ans.append(0)
            stack.append([node.val, i])
            node = node.next
            i += 1

        return ans

    def nextLargerNodes_1(self, head): # Works, other solution is faster

        if not head: return []

        d = {}
        stack = deque()
        node = head
        i = 0

        while node:
            while stack and stack[-1][0] < node.val:
                n = stack.pop()
                d[n[1]] = node.val

            stack.append([node.val, i])

            node = node.next
            i += 1


        ans = []

        for z in range(i):
            if z in d:
                ans.append(d[z])

            elif z not in d:
                ans.append(0)

        return ans



        # then, for nodes that have no match, pop and d[node] = 0

        # then loop through again, form ans = [], return ans

def createLL(arr):
    nodes = []

    for e in arr:
        nodes.append(ListNode(e))

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    return nodes[0]

if __name__ == '__main__':
    s = Solution()

    ll = createLL([1,2,3,4])

    ll

    # print(s.nextLargerNodes(createLL([2,1,5])))
    # print(s.nextLargerNodes(createLL([2,7,4,3,5])))
    # print(s.nextLargerNodes(createLL([1,7,5,1,9,2,5,1])))
    # print(s.nextLargerNodes(createLL([1,2,3,4,5,6])))
    # print(s.nextLargerNodes(createLL([5,4,3,2,1])))
    # print(s.nextLargerNodes(None))
    # print(s.nextLargerNodes(createLL([1,2,3,1,2,3])))
