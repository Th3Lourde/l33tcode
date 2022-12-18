'''
a<--b   c-->d-->e-->f
    1   2

tmp = 2.next
2.next = 1
1 = 2
2 = t


# Special Case for the head

1 <-- 2 <-- 3 <-- 4     None
                  1      2
'''

class Solution:
    def reverseList(self, head):
        if not head:
            return head

        if not head.next:
            return head

        # handle head case
        ptr1 = head.next
        ptr2 = head.next.next

        head.next = None
        ptr1.next = head

        while ptr1 and ptr2:
            t = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = t

        return ptr1
