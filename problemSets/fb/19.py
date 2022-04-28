'''
Get length of linkedList
calc how many times we need to travel (length-n-1)


start at head
traverse n-1 times to the right

set node(n-1).next = node(n+1)
edge case for when we are deleting the last node in the ll

return head
'''

class Solution:
    def removeNthFromEnd(self, head, n):
        llLen = 0
        node = head

        while node:
            llLen += 1
            node = node.next

        if llLen == 1 and n == 1:
            return None

        stepsRight = llLen-n-1

        if stepsRight < 0:
            return head.next

        node = head

        for _ in range(stepsRight):
            node = node.next

        print(node.val)

        if node.next == None:
            node.next = None
        else:
            node.next = node.next.next

        return head
