'''
You are given two linked lists list1 and list2

Each list is sorted, return a linked list that is list1+list2 that is also
sorted in ascending order.

[1,2,4]
[1,3,4]


'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2
        resp = None

        # Populate resp
        if p1 and p2:
            if p1.val <= p2.val:
                resp = ListNode(p1.val)
                p1 = p1.next
            else:
                resp = ListNode(p2.val)
                p2 = p2.next
        elif p1:
                resp = ListNode(p1.val)
                p1 = p1.next
        elif p2:
                resp = ListNode(p2.val)
                p2 = p2.next
        else:
            return None

        print(head.val)

        head = resp

        while p1 and p2:
            if p1.val <= p2.val:
                node = ListNode(p1.val)

                resp.next = node
                resp = resp.next

                print(node.val)

                p1 = p1.next

            else:
                node = ListNode(p2.val)
                print(node.val)

                resp.next = node

                resp = resp.next

                p2 = p2.next

        while p1:
            node = ListNode(p1.val)
            print(node.val)

            resp.next = node
            resp = resp.next

            p1 = p1.next

        while p2:
            node = ListNode(p2.val)

            resp.next = node
            resp = resp.next

            p2 = p2.next

        return head
