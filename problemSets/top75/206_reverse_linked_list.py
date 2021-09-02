'''
Given a linked list, reverse it.

1 <-- 2 --> 3 --> 4 --> 5
l     m     r

5 --> 4 --> 3 --> 2 --> 1
'''



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}-->{}".format(self.val, self.next)

        # len(arr) >= 1
def makeLL(arr):
    head = ListNode(arr[0])
    node = head

    for idx in range(1, len(arr)):
        node.next = ListNode(arr[idx])
        node = node.next

    return head

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        l = head
        m = head.next

        if not m.next:
            l.next = None
            m.next  = l
            return m

        r = m.next

        l.next = None
        m.next = l

        while r:
            tR = r.next
            r.next = m

            m = r
            r = tR

        return m

print(Solution().reverseList(None))
print(Solution().reverseList(makeLL([1])))
print(Solution().reverseList(makeLL([1,2])))
print(Solution().reverseList(makeLL([1,2,3,4,5,6,7])))
