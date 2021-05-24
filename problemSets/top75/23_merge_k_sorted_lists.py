import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []

        for listNode in lists:
            while listNode:
                heapq.heappush(heap, listNode.val)
                listNode = listNode.next

        if not heap:
            return None

        head = ListNode(heapq.heappop(heap))
        ptr = head

        while heap:
            ptr.next = ListNode(heapq.heappop(heap))
            ptr = ptr.next

        return head
