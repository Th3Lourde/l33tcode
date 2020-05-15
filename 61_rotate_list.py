
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{}-->{}".format(self.val, self.next)
        # return "{}".format(self.val)

    def __repr__(self):
        return "{}".format(self.val)

class Solution:

    def rotateRight(self, head, k): # Just took the same approach as before. Whoops.
        if k == 0 or head == None:
            return head

        n = 1
        p1N = head.next
        p2N = head
        connected = False

        while True:

            if n == k:
                p1N = p1N.next
                p2N = p2N.next
                p2N.next = None

                ans = p1N

                if connected:
                    return ans

                while p1N.next != None:
                    p1N = p1N.next

                p1N.next = head

                return ans

            elif p1N == None:
                k = k % n

                if k == 0:
                    return head

                p2N.next = head
                connected = True

                n = 1
                p1N = head.next
                p2N = head

            else:
                p1N = p1N.next
                p2N = p2N.next
                n += 1



    def rotateRight_2(self, head, k): # No dice
        if k == 0 or head == None:
            return head

        connected = False
        p1 = 1
        p1_n = head.next
        p2_n = head

        # while p1_n != None and p1 != k:
        while True:

            if p1 == k:
                p2_n.next = None

                if connected:
                    return p1_n

                ans = p1_n

                while p1_n.next != None:
                    p1_n = p1_n.next

                p1_n.next = head

                return ans


            elif p1_n == None:
                k = k%(p1)

                if k == 0:
                    return head

                p2_n.next = head
                connected = True

                p2_n = p2_n.next
                p1_n = p2_n.next
                p1 = 1

            else:
                p1_n = p1_n.next
                p2_n = p2_n.next
                p1 += 1




    # Run-Time: O(n)
    # Memory-Complexity: O(n)
    def rotateRight_1(self, head, k):
        if k == 0 or head == None:
            return head

        n = 0
        d = {}
        tmp = head

        while tmp != None:
            d[n] = tmp
            tmp = tmp.next
            n += 1

        k = k % n

        if k == 0:
            return head

        d[n-1].next = d[0] # Connect the end to the front
        d[n-k-1].next = None # Set the previous node to None
        return d[n-k]


if __name__ == '__main__':
    s = Solution()

    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    a.next = b
    b.next = c
    c.next = d
    # d.next = e
    # e.next = f

    print("[input]: {}".format(a))

    # i = 2

    # print("[a,{}] {}".format(i, s.rotateRight(a,i)))

    for i in range(5):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)

        a.next = b
        b.next = c
        c.next = d

        print("[a,{}] {}".format(i, s.rotateRight(a,i)))
