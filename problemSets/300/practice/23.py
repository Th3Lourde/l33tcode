# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists):
        q = PriorityQueue()

        for idx, ll in enumerate(lists):
            if ll != None:
                q.put((ll.val, idx, ll))

        head = None
        node = None

        while q.qsize() > 0:
            val, idx, qNode = q.get()

            # print("popped: {}".format(val))

            # append to list
            if head == None:
                head = ListNode(val=val)
                node = head
            else:
                new_node = ListNode(val=val)
                node.next = new_node
                node = node.next

            if qNode.next:
                # print("putting {}".format(qNode.next.val))
                q.put((qNode.next.val, idx, qNode.next))
                # print(q.qsize())

        return head
