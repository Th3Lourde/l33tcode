'''
Given two linked lists
linked lists are sorted

Return the head of a linked list
where the head is composed of all nodes
in the two linked lists that we are given,
returned in a sorted manner.

example run-through

1,2,4
      ^

1,3,4
      ^

1 --> 1 --> 2 --> 3 --> 4 --> 4
                              ^
nodeToAdd = 4



list1 dne
list2 dne
list1, list 2 dne


'''

class Solution:
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2
        respHead = None
        p3 = None

        if not list1 and not list2:
            return None

        while p1 or p2:
            nodeToAdd = None

            if p1 != None and p2 != None:
                if p1.val < p2.val:
                    nodeToAdd = p1
                    p1 = p1.next
                else:
                    nodeToAdd = p2
                    p2 = p2.next

            elif p1 != None:
                nodeToAdd = p1
                p1 = p1.next
            elif p2 != None:
                nodeToAdd = p2
                p2 = p2.next

            if p3 == None:
                respHead = ListNode(nodeToAdd.val)
                p3 = respHead
            else:
                p3.next = ListNode(nodeToAdd.val)
                p3 = p3.next

        return respHead
