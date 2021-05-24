
'''
There's a 'better' solution
where you try to make one of
the pointers run into each other
link: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
'''


class Solution:
    def getIntersectionNode_1(self, headA, headB):
        if headA == None:
            return None

        if headB == None:
            return None

        headA.val = str(headA.val)

        if type(headB.val) == str:
            headB.val = int(headB.val)

            # Should be redundant
            headA.val = int(headA.val)

            return headB

        headB.val = str(headB.val)

        # if headA.next == None:
        #     headA.val = int(headA.val)
        #     headB.val = int(headB.val)
        #     return None
        #
        # if headB.next == None:
        #     headB.val = int(headB.val)
        #     headA.val = int(headA.val)
        #     return None

        tmpA = headA.next
        tmpB = headB.next
        ans = None


        # Find intersection,
        # if exists, put it at ans
        while True:
            if tmpA != None:

                if type(tmpA.val) == str:
                    tmpA.val = int(tmpA.val)
                    ans = tmpA
                    break

                tmpA.val = str(tmpA.val)

                tmpA = tmpA.next

            if tmpB != None:
                if type(tmpB.val) == str:
                    tmpB.val = int(tmpB.val)
                    ans = tmpB
                    break

                tmpB.val = str(tmpB.val)

                tmpB = tmpB.next

            if tmpA == None and tmpB == None:
                break


        # Clean up input
        tmpA = headA
        tmpB = headB

        while type(tmpA.val == str):
            tmpA.val = int(tmpA.val)
            if tmpA.next != None:
                tmpA = tmpA.next

            elif tmpA.next == None:
                break

        while type(tmpB.val == str):
            tmpB.val = int(tmpB.val)
            if tmpB.next != None:
                tmpB = tmpB.next

            elif tmpB.next == None:
                break

        return ans

    def getIntersectionNode_2(self, headA, headB):

        if headA == None:
            return None

        if headB == None:
            return None

        headA.val = str(headA.val)

        if type(headB.val) == str:
            headB.val = int(headB.val)

            # Should be redundant
            headA.val = int(headA.val)

            return headB

        headB.val = str(headB.val)

        if headA.next == None:
            headA.val = int(headA.val)
            headB.val = int(headB.val)
            return None

        if headB.next == None:
            headB.val = int(headB.val)
            headA.val = int(headA.val)
            return None

        tmpA = headA.next
        tmpB = headB.next
        ans = None

        while True:

            if type(tmpA.val) == str:
                tmpA.val = int(tmpA.val)
                ans = tmpA
                break

            tmpA.val = str(tmpA.val)

            if tmpA.next != None:
                tmpA = tmpA.next


            if type(tmpB.val) == str:
                tmpB.val = int(tmpB.val)
                ans = tmpB
                break



            if tmpB.next != None:
                tmpB.val = str(tmpB.val)
                tmpB = tmpB.next

            if tmpA.next == None and tmpB.next == None:
                break

        tmpA = headA
        tmpB = headB

        while type(tmpA.val == str):
            tmpA.val = int(tmpA.val)
            if tmpA.next != None:
                tmpA = tmpA.next

            elif tmpA.next == None:
                break

        while type(tmpB.val == str):
            tmpB.val = int(tmpB.val)
            if tmpB.next != None:
                tmpB = tmpB.next

            elif tmpB.next == None:
                break

        return ans

    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        node_a = headA
        aLoop = 0
        node_b = headB
        bLoop = 0

        while aLoop <= 2 and bLoop <= 2:
            if node_a == node_b:
                return node_a

            if node_a.next == None:
                node_a = headB
                aLoop += 1

            else:
                node_a = node_a.next

            if node_b.next == None:
                node_b = headA
                bLoop += 1
            else:
                node_b = node_b.next

        return None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{} --> {}".format(self.val, self.next)


if __name__ == '__main__':
    a1 = ListNode(4)
    a2 = ListNode(1)

    a1.next = a2

    b1 = ListNode(5)
    b2 = ListNode(0)
    b3 = ListNode(1)

    b1.next = b2
    b2.next = b3

    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)

    c1.next = c2
    c2.next = c3

    a2.next = c1

    b3.next = c1

    print(a1)
    print(b1)

    s = Solution()
    r = s.getIntersectionNode(a1, b1)
    print(r)
