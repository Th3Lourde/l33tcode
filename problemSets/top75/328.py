'''
Ok so we should do this with o(n) time complexity and o(1) space
complexity.

Create two sublists, one for even nodes and one for odd nodes


'''

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        nodeNum = 3

        oddHead = head
        oddNode = oddHead
        evenHead = head.next
        evenNode = evenHead

        node = head.next.next

        while node:
            if nodeNum % 2 == 1:
                oddNode.next = node
                oddNode = oddNode.next
            else:
                evenNode.next = node
                evenNode = evenNode.next

            node = node.next
            nodeNum += 1

        oddNode.next = evenHead
        evenNode.next = None

        return oddHead
