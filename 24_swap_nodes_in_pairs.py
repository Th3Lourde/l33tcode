
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{}-->{}".format(self.val, str(self.next))

class Solution:
    def swapPairs(self, head):
        print("[Initial] {}".format(head))

        if head == None:
            return head

        elif head.next == None:
            return head

        n = head.next.next
        h = head.next
        h.next = None

        ans = h
        h.next = head
        h.next.next = None

        p = ans.next

        while n != None:
            a = n

            if a.next == None:
                p.next = a

                return ans

            b = a.next
            n = b.next

            p.next = b
            b.next = a
            a.next = None
            p = a

        return ans

if __name__ == '__main__':
    s = Solution()

    a = Node(1)
    b = Node(2)
    # c = Node(3)
    # d = Node(4)
    # e = Node(5)
    # f = Node(6)

    a.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    # e.next = f

    print("[After] {}".format(s.swapPairs(a)))
