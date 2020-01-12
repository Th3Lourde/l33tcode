
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # two-pass solution
    # run-time: O(n^2)
    # memory complexity: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        len = 0
        node = head

        while node:
            len += 1
            node = node.next

        target = len-n

        if target == 0:
            return head.next

        tmp = 0
        node = head

        while tmp < target-1: # get to node before target
            node = node.next
            tmp += 1

        if n == 1:
            node.next = None
            return head

        elif n != 1:
            tmp = node
            node =  node.next.next
            tmp.next = node
            return head



    # run-time: O(n)
    # memory complexity: O(n)
    def removeNthFromEnd_1(self, head: ListNode, n: int) -> ListNode:
        node = head
        llnodes = []

        while node:
            llnodes.append(node)
            node = node.next

        target = len(llnodes) - n

        if target == 0:
            return head.next

        elif target == len(llnodes)-1:
            llnodes[-2].next = None
            return head

        elif 0 < target and target < len(llnodes)-1:
            llnodes[target-1].next = llnodes[target+1]
            return head
