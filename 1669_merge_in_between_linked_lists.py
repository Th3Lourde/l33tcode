

class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        pA = list1
        pB = list1

        for i in range(b+1):
            pB = pB.next

        for i in range(a-1):
            pA = pA.next

        # In position to insert list2
        pA.next = list2

        while pA.next != None:
            pA = pA.next

        pA.next = pB

        return list1
