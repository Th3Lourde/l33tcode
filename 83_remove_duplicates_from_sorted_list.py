
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p1 = p2 = head

        while p2:
            if p2.val == p1.val:
                p2 = p2.next

            elif p2.val != p1.val:
                p1.next = p2
                p1 = p2
                p2 = p2.next

        if p1:
            p1.next = None

        return head
