
'''
[1,2,3]
[1,2,3,3]
[1,2,3,3,3]


[1,2,3,3,4]

[1,1,2,3,4]

[1,2,3,4]

[1,1,2,3,3,4,5,6]

[1,2,3,3,4,5,6,6]

'''

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
    def deleteDuplicates(self, head): # No dice
        if not head:
            return head

        p1 = head

        if not p1.next:
            return head

        if p1.val == p1.next.val: # The initial node is a repeat
            p2 = p1.next

            while p2: # Find a valid head

                if p2.val == p1.val:
                    if not p2.next:
                        return None

                    p2 = p2.next

                elif p2.val != p1.val:
                    # We have found a node that has a new value
                    # Check to see if it itself is also a repeat

                    if not p2.next:
                        return p2

                    elif p2.val == p2.next.val:
                        p1 = p2
                        p2 = p2.next

                    elif p2.val != p2.next.val: # We have found a valid head
                        head = p2
                        break

            if head.val == head.next.val:
                return None

        # If we got here, we have a valid head that doesn't have
        # any repeats
        p1 = p2 = head.next

        if not p1.next:
            return head

        p0 = head

        p0.next = None

        p2 = p1.next

        while p2:
            # print("[head]: {}".format(head))
            # print("[p0]: {}".format(p0))
            # print("[p1]: {}".format(p1))
            # print("[p2]: {}".format(p2))
            # print("--------")

            if p1.val != p2.val: # nodes don't have the same value

                p0.next = p1

                p1.next = p2 # Do I need this?

                p1 = p1.next
                p2 = p2.next
                p0 = p0.next

            elif p1.val == p2.val: # found repeat node, need to find non-repeat node

                p0.next = None

                if p2.next == None:
                    return head

                while p2:

                    if p2.val == p1.val:
                        p2 = p2.next

                    elif p2.val != p1.val:

                        if p2.next == None:
                            p0.next = p2
                            return head

                        if p2.val == p2.next.val:
                            p1 = p2
                            p2 = p2.next

                        elif p2.val != p2.next.val:
                            p0.next = p2
                            p0 = p0.next
                            p1 = p2.next

                            if p1.next == None:
                                # p0.next = None
                                p0.next = p1
                                # print("h")
                                return head

                            p0.next = None
                            p2 = p1.next

                            break
        return head


if __name__ == '__main__':
    s = Solution()

    testCases = [
        [[],[]],
        [[1,2,3], [1,2,3]],
        [[1,2,3], [1,2,3]],
        [[1,2,3,3], [1,2]],
        [[1,1,2,3], [2,3]],
        [[1,1,2,2,3,3], []],
        [[1,2,3,3,3], [1,2]],
        [[1,2,3,3,3,4,5,6,6], [1,2,4,5]],
        [[1,2,2,2,3,4,4,4], [1,3]],

        [[0,1,2,2,3,4], [0,1,3,4]],

        # B
        [[0,1,1,2,3,4], [0,2,3,4]],


        # B
        [[0,1,1,1,2,3,4], [0,2,3,4]],

        # M
        [[0,1,2,2,3,4], [0,1,3,4]],

        # M
        [[0,1,2,2,2,3,4], [0,1,3,4]],

        # E
        [[0,1,2,3,4,4,5,5,6], [0,1,2,3,6]],

        # E
        [[0,1,2,3,4,4], [0,1,2,3]],

        # B M
        [[0,1,1,2,3,3,4], [0,2,4]],

        # B E
        [[0,1,1,2,3,4,4], [0,2,3]],

        # M E
        [[0,1,2,2,3,4,4], [0,1,3]],

        # B M E
        [[0,1,1,2,3,4,4], [0,2,3]],

        [[0,1,2,2,3,3,4], [0,1,4]],

        [[0,0,1,2,2,3,3,4], [1,4]],

        [[0,1,2,2,2,3,4], [0,1,3,4]],

        [[0,1,2,2,2,3,4,4,5,6], [0,1,3,5,6]],

        [[0,1,2,2,2,3,4,4,5,6,7,7], [0,1,3,5,6]],

        [[0,1,2,2,2,3,4,4,5,6,6,7,7], [0,1,3,5]],

        [[0,1,2,2,2,3,4,4,5,6,6,6,7,8,8], [0,1,3,5,7]],

        [[0,1,2,2,2,3,4,4,5,6,6,6,7,8], [0,1,3,5,7,8]],

    ]

    for tc in testCases:

        a = LinkedList(tc[0])
        b = LinkedList(tc[1])

        a.head = s.deleteDuplicates(a.head)

        assert str(a.head) == str(b.head), ".del({}) --> [{}] != [{}]".format(tc[0], a.head, b.head)

    print("[passed all test cases]")
