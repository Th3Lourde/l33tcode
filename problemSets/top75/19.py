'''
Loop through list once, get the length
the node you want to remove is length - n

loop through list, keeping track of the previous element
# edge case if first node is the element if we want to delete
# edge case if last node is the element we want to delete

set prev.next = node.next
set node.next to none
done
'''

'''
l = 5
t = 5

1 --> 2 --> 3 --> 4 --> 5
'''

class Solution:
    def removeNthFromEnd(self, head, n):
        # if target node is the first node
        # get length of ll
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        print(length)

        target = length-n+1

        print(target)

        # if target is the first node
        if target == 1:
            return head.next

        nodeNum = 2
        prev = head
        node = head.next

        while nodeNum != target:
            prev = prev.next
            node = node.next
            nodeNum += 1

        if n == length:
            prev.next = None
        # if target node is the last node
        # if target node is in the middle
        else:
            prev.next = node.next

        return head
