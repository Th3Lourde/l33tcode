
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None

        head.val = str(head.val)

        if type(head.next) == str:
            headv.val = int(head.val)
            return head

        tmp = head
        headv = head.next

        while True:
            if type(headv.val) == str:
                # tmp.val = int(tmp.val)
                # return tmp

                headv.val = int(headv.val)
                return headv
            elif type(headv.val) == int:
                headv.val = str(headv.val)
                if  headv.next == None:
                    return None
                elif headv.next != None:
                    tmp = headv
                    headv = headv.next

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    s = Solution()

    # fuzz()

    r = s.detectCycle(a)
    # print(r)
    print(r.val)
