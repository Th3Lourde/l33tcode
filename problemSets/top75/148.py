class Solution:
    def sortList(self, head):
        if not head or not head.next: return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, head1, head2):
        dummy = tail = ListNode(None)

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                tail = tail.next
                head2 = head2.next

        tail.next = head1 or head2
        return dummy.next
