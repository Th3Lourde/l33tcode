
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "{} --> {}".format(self.val, str(self.next))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tens = 0

        n1 = l1
        n2 = l2

        ans = ListNode(0)
        a = ans

        while True:
            tmp = n1.val + n2.val + tens

            if tmp >= 10:
                ans.val = tmp-10
                tens = tmp//10

            elif tmp < 10:
                ans.val = tmp
                tens = 0

            if (n1.next != None) and (n2.next != None):
                n1 = n1.next
                n2 = n2.next
            elif (n1.next != None) and (n2.next == None):
                # Finished n2, follow n1
                n2.val = 0
                n1 = n1.next
            elif (n1.next == None and n2.next != None):
                # Finished n1, follow n2
                n1.val = 0
                n2 = n2.next
            elif (n1.next == None and n2.next == None):
                # Done with both lists
                # ans.next = None

                if tens == 0:
                    return a
                elif tens != 0:
                    ans.next = ListNode(tens)
                    return a


            ans.next = ListNode(0)
            ans = ans.next


if __name__ == '__main__':
    # List one
    # a1 = ListNode(2)
    # b1 = ListNode(4)
    # c1 = ListNode(3)
    #
    # a1.next = b1
    # b1.next = c1
    # c1.next = None
    #
    # a2 = ListNode(5)
    # b2 = ListNode(6)
    # c2 = ListNode(4)
    #
    # a2.next = b2
    # b2.next = c2
    # c2.next = None

    a1 = ListNode(5)
    a2 = ListNode(5)

    s = Solution()

    r = s.addTwoNumbers(a1, a2)
    print(r)
