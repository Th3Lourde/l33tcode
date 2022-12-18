'''
Given the head of a linked list, rotate it to the right by k places.


1) Get the length of the linked list
2) Mod k by the length of the linked list
3) So the node-k is the new head
|--> if k == len of ll, do nothing
|--> else, cut the ll b4 the new head
|--> go to the end of the new head, point it to old head



'''

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None

        n = 0
        node = head

        while node:
            n += 1
            node = node.next

        k = k%n
        if k == 0:
            return head

        # first node is the last node
        targetNode = n-(k-1)
        node = head

        # print(targetNode)

        for _ in range(targetNode-2):
            node = node.next

        # split off and store the new head
        newHead = node.next
        # print(newHead)
        node.next = None
        # print(newHead)

        # continue to end
        node = newHead

        while node.next:
            node = node.next

        node.next = head

        return newHead
