

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{}-->{}".format(self.val, self.next)


class Solution:
    def reverseList_i(self, head):
        if head == None or head.next == None:
            return head

        past = head
        current = head.next
        past.next = None

        while True:
            future = current.next
            current.next = past

            if future == None:
                return current

            elif future != None:
                past = current
                current = future

    def reverseList_r(self, head):
        if head == None or head.next == None:
            return head

        past = head
        current = head.next
        past.next = None

        def helper(past, current):
            future = current.next
            current.next = past
            if future == None:
                return current
            elif future != None:
                return helper(current, future)

        return helper(past,current)

if __name__ == '__main__':
    s = Solution()

    tail = ListNode(0)
    a = ListNode(1)
    b = ListNode(2)

    tail.next = a
    a.next = b

    print("start: {}".format(tail))

    tail = s.reverseList_r(tail)

    print("end: {}".format(tail))
