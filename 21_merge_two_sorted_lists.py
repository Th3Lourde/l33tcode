
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{} --> {}".format(self.val, str(self.next))


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None or l2 == None:
            if l1 == None and l2 == None:
                return None

            elif l1 == None:
                return l2

            elif l2 == None:
                return l1

        if l1.val == l2.val:
            p1 = l1
            p2 = l2
            p3 = l1.next

        elif l1.val < l2.val:
            p1 = l1
            p2 = l2
            p3 = l1.next

        elif l1.val >= l2.val:
            p1 = l2
            p2 = l1
            p3 = l2.next


        if p3 == None:
            p1.next = p2
            return p1

        ans = p1

        while p2 != None:
            if p3.val > p2.val:
                p1.next = ListNode(p2.val)
                p1 = p1.next
                p1.next = p3

                p2 = p2.next

            elif p3.val <= p2.val:
                p3 = p3.next
                p1 = p1.next

                if p3 == None:
                    p1.next = p2
                    break

        return ans




if __name__ == '__main__':
    '''
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    '''

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(4)

    ll2 = ListNode(1)
    ll2.next = ListNode(3)
    ll2.next.next = ListNode(4)

    s = Solution()

    print(s.mergeTwoLists(ll1, ll2))
