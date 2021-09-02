class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

def makeLL(arr):
    head = ListNode(arr[0])
    node = head

    for idx in range(1, len(arr)):
        node.next = ListNode(arr[idx])
        node = node.next

    return head

class Solution:
    def removeNthFromEnd(self, head, n):
        def getLength(node):
            length = 0

            while node:
                node = node.next
                length += 1

            return length

        length = getLength(head)

        if length-n == 0:
            return head.next

        l = head

        for i in range(length-n-1):
            l = l.next

        r = l.next.next

        if r:
            l.next = r

        else:
            l.next = None

        return head

print(Solution().removeNthFromEnd(makeLL([1,2,3,4,5]), 5))
# print(Solution().removeNthFromEnd(makeLL([1,2]), 1))
