'''
Given a linked list and a value x,
partition it ∋ in a quick sort
fashion

Ok so have a less and a greater head

Also have a head for greater, that is where
we could put the repeats
at the head of the greater than values.

l = None
g = None
node = head

1 → 4 → 3 → 2 → 5 → 2, x=3
^

1 < 3
l = 1
lHead = l
lTail = l
node = node.next

1 → 4 → 3 → 2 → 5 → 2, x=3
    ^

4 > 3
r = 4
rHead = 4
rTail = 4

lHead = l
lTail = l
rHead = 4
rTail = 4

1 → 4 → 3 → 2 → 5 → 2, x=3
        ^

3 == 3
r = ListNode(3)
r.next = rHead
rHead = r

l = 1
r = 3 --> 4

lHead = l
lTail = l
rHead = 3
rTail = 4

1 → 4 → 3 → 2 → 5 → 2, x=3
            ^


l = 1 --> 2
r = 3 --> 4


lHead = l
lTail = 2
rHead = 3
rTail = 4


1 → 4 → 3 → 2 → 5 → 2, x=3
                ^

l = 1 --> 2
r = 3 --> 4 --> 5

1 → 4 → 3 → 2 → 5 → 2, x=3
                    ^

l = 1 --> 2 --> 2
r = 3 --> 4 --> 5

lTail.next = rHead

return lHead

Ok so edge cases.

What if one of the ll is empty?

only elements greater
only elements less than
only elements equal to
mix of both

others?

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

def generateLL(arr):
    nodes = []

    for e in arr:
        nodes.append(ListNode(e))

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    return nodes[0]

class Solution:
    def partition(self, head, x): # Done
        lHead = None
        lTail = None
        rHead = None
        rTail = None

        node = head

        while node:
            # do a thing
            if node.val < x:
                if not lHead and not lTail:
                    lHead = lTail = ListNode(node.val)

                else:
                    lTail.next = ListNode(node.val)
                    lTail = lTail.next

            elif not rHead and not rTail:
                rHead = rTail = ListNode(node.val)

            # elif node.val == x:
            #     tmp = ListNode(node.val)
            #     tmp.next = rHead
            #     rHead = tmp

            elif node.val >= x:
                rTail.next = ListNode(node.val)
                rTail = rTail.next

            node = node.next

        if lHead:
            lTail.next = rHead
            return lHead

        return rHead


if __name__ == '__main__':
    s = Solution()

    ll = generateLL([1,4,3,2,5,2])

    # ll

    # s.partition(ll, 3)

    # s.partition(generateLL([1,2,2,2]), 3)
    # s.partition(generateLL([3,4,5]), 3)
    s.partition(generateLL([5,4,3,2,1]), 5)
    s.partition(None, 5)
