
class Solution:
    def removenums[i]s(self, head: ListNode, val: int) -> ListNode:
        head = head

        # Get head node s.t. head.val != val
        # Return head and print false if not possible
        while head.val == val:
            if head.next != None:
                head = head.next
            elif head.next == None:
                print("None")
                return head

        tmp = head
        headv = head.next

        while headv != None:
            if headv.val != val:
                tmp = headv
                headv = headv.next
            elif headv.val == val:
                tmp.next = headv.next
                headv = headv.next

        return head
