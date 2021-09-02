# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
L0 → L1 → … → Ln - 1 → Ln
'''

'''
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
'''

'''
So first node, last node, second node, second to last node, ...
Modify the list in-place.

So how can we do this? We can copy the linked list into a dict
and then modify the .next property of the different.

That could work. What else could we do?
We could reverse half of the list and then traverse in a smart
way

1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8
            l
                  r

If even, divide by two
If odd, subtract one,

if even, the node that the traversal will stop at is:
length of ll/2

if odd, the node that the traversal will stop at is:
length of (ll-1)/2 + 1

Reverse 0 to node that this will stop at.

1 --> 8 --> 2 --> 7 --> 3 --> 4
            ^     |

5 <-- 6 <-- 7 <-- 8
      ^

0) Find length of linked list
1) Find the 'middle' of the ll
2) Reverse nodes from middle onwards
3) Put the nodes back together
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

def makeLL(arr):
    head = ListNode(arr[0])
    node = head

    for idx in range(1, len(arr)):
        node.next = ListNode(arr[idx])
        node = node.next

    return head

class Solution:
    def reorderList(self, head):
        if not head:
            return head

        if not head.next:
            return head

        # 0 find the length of the ll
        def findLength(node):
            if not node:
                return 0

            length = 0

            while node:
                length += 1
                node = node.next

            return length

        n = findLength(head)

        # 1 find middle value
        m = 0

        if n % 2 == 0:
            m = int(n/2)
        else:
            m = int((n-1)/2 + 1)

        # 2 reverse nodes from m --> n
        end = head
        start = head.next


        for i in range(m-1):
            end = end.next
            start = start.next


        end.next = None


        def reverseLL(node):
            if not node or not node.next:
                return node

            elif not node.next.next:
                # len = 2
                a = node
                b = node.next

                b.next = a
                a.next = None

                return b

            head = node

            l = node
            m = node.next
            r = m.next
            l.next = None

            while r:
                m.next = l
                l = m
                m = r
                r = r.next

            m.next = l

            return m

        # 3 put the lists back together
        p1 = head
        p2 = reverseLL(start)

        while p2 and p1:
            tmp = p1.next
            p1.next = p2
            p2 = p2.next
            p1.next.next = tmp
            p1 = tmp

        return head

print(Solution().reorderList(makeLL([1,2,3,4,5,6,7,8])))
print(Solution().reorderList(makeLL([1,2,3,4,5,6,7])))
