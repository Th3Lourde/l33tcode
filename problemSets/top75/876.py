'''
Given the head of a singly linkedlist, return the middle node
1) Find the length of the ll
2) Find the length of the middle node
'''

int(6/2)
int(5/2)


class Solution:
    def middleNode(self, head):
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        node = head

        for _ in range(int(length/2)):
            node = node.next

        return node
