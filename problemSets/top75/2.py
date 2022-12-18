class Solution:
    # return list node
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        larger = l1
        smaller = l2

        l1Count = 0
        l2Count = 0
        n1 = l1
        n2 = l2

        # Test if smaller > larger
        while n2:
            l2Count += 1
            n2 = n2.next

            if n1:
                l1Count += 1
                n1 = n1.next

        if l2Count > l1Count:
            larger = l2
            smaller = l1

        carry = 0
        n1 = larger
        n2 = smaller

        while n1:
            if n2:
                ones = n1.val + n2.val + carry
                carry = 0

                if ones >= 10:
                    ones -= 10
                    carry += 1

                n1.val = ones
                n2 = n2.next

            else:
                ones = n1.val + carry
                carry = 0

                if ones >= 10:
                    ones -= 10
                    carry += 1

                n1.val = ones

            n1 = n1.next

        if carry:
            # Go to the last node, add a node with a one
            n = larger

            while n.next:
                n = n.next

            n.next = ListNode(1)

        return larger
