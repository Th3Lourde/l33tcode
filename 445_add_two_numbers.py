
class LinkedListNode:
    def __init__(self, x, next=None, prev=None):
        self.val = x
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "{}-->{}".format(self.val, str(self.next))

class LinkedList:
    def __init__(self, values):
        self.__size = 0
        self.head = None
        self.tail = None

        if len(values) != 0:

            for value in values:

                if self.head == None:
                    self.head = LinkedListNode(value)
                    self.tail = self.head

                    self.__size += 1

                elif self.head != None:
                    tmp = LinkedListNode(value)

                    self.tail.next = tmp
                    tmp.prev = self.tail

                    self.tail = self.tail.next

                    self.__size += 1


    def equals(self, vals):
        # given list of values, check that ll matches the list.
        # returns True or False

        if self.size() != len(vals):
            print("[dne] {Size difference}")
            return False

        elif self.size() == 0 and len(vals) == 0:
            return True

        elif self.size() == 1 and len(vals) == 1:
            if self.head.prev == None and self.head.val == vals[0] and self.head.next == None:
                return True

            else:

                if self.head.prev != None:
                    print("[dne] {head != None}")

                if self.head.val != vals[0]:
                    print("[dne] {head.val != vals[0]}")

                if self.head.next != None:
                    print("[dne] {head.next != None}")

                return False

        head = self.head

        for i in range(len(vals)):

            if i == 0:
                if not(head.prev == None) or not(head.val == vals[i]) or not(head.next.val == vals[i+1]):

                    if not(head.prev == None):
                        print("[dne] {head.prev != None}")

                    if not(head.val == vals[i]):
                        print("[dne] {head.val != vals[i]}")

                    if not(head.next.val == vals[i+1]):
                        print("[dne] {head.next.val != vals[i+1]}")

                    return False

            elif i > 0 and i < len(vals)-1:
                if not(head.prev.val == vals[i-1]) or not(head.val == vals[i]) or not(head.next.val == vals[i+1]):

                    if not(head.prev.val == vals[i-1]):
                        print("[dne] {head.prev.val != vals[i-1]}")

                    if not(head.val == vals[i]):
                        print("[dne] {head.val != vals[i]}")

                    if not(head.next.val == vals[i+1]):
                        print("[dne] {head.next.val != vals[i+1]}")

                    return False

            elif i > 0 and i == len(vals)-1:
                if not(head.prev.val == vals[i-1]) or not(head.val == vals[i]) or not(head.next == None):

                    if not(head.prev.val == vals[i-1]):
                        print("[dne] {head.prev.val != vals[i-1]}")

                    if not(head.val == vals[i]):
                        print("[dne] {head.val != vals[i]}")

                    if not(head.next == None):
                        print("[dne] {head.next == None}")

                    return False

            head = head.next

        return True


class Solution:
    def addTwoNumbers(self, l1, l2):

        s1 = []
        s2 = []

        while l1:
            s1.append(l1)
            l1 = l1.next

        while l2:
            s2.append(l2)
            l2 = l2.next

        max = s1
        min = s2

        if len(s2) > len(s1):
            max = s2
            min = s1

        ones = 0
        head = max[0]

        while min != []:

            val_new = max.pop()
            sum = val_new.val + min.pop().val + ones
            ones = 0

            if sum % 10 != sum:
                sum = sum % 10
                ones = 1

            val_new.val = sum

        if max != [] and ones == 1:
            val_new = max.pop()
            val_new.val += 1

            if val_new.val % 10 != val_new.val:
                val_new.val = val_new.val%10

            elif val_new.val % 10 == val_new.val:
                return head

            ones = 1

            while max != []:
                t = max.pop()
                t.val += 1

                if t.val < 10:
                    return head

                t.val = t.val%10

        if max == [] and ones == 1:
            return LinkedListNode(1, head)

        return head


if __name__ == '__main__':
    s = Solution()

    testCases = [
        # Same length, ones = 0
        [[1,2,3], [1,2,3], [2,4,6]],

        # Same length, ones = 1
        [[1,2,3], [9,2,3], [1,0,4,6]],

        # Same length, ones = 1
        [[9,1,9], [1,9,1], [1,1,1,0]],

        # Same length, ones = 1, multiple carries
        [[9,1,9], [1,8,1], [1,1,0,0]],

        # Different length, ones = 0
        [[7,2,4,3], [9,6,4], [8,2,0,7]],

        # Different length, ones = 1
        [[7,2,4,3], [5,6,4], [7,8,0,7]],

        # Different length, ones = 1
        [[7,9,4,3], [6,4], [8,0,0,7]],

        # Different length, ones = 1
        [[9,9,4,3], [6,4], [1,0,0,0,7]],
    ]


    for tc in testCases:
        resp = s.addTwoNumbers(LinkedList(tc[0]).head, LinkedList(tc[1]).head)
        ans = LinkedList(tc[2]).head

        assert str(resp) == str(ans), "[{}] != [{}] |:O".format(resp, ans)


    print("[passed all test cases]")
