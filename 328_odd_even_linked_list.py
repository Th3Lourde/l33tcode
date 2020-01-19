
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{} --> {}".format(self.val, str(self.next))


class Solution:

    def oddEvenList(self, head):
        p1 = head
        p2 = head.next
        p2_head = p2

        if head == None:
            return head

        if p2 == None:
            return head

        iterate = True
        iterator = p2

        while iterator != None:
            if iterate:
                iterator = iterator.next
                if iterator != None:
                    p1.next = iterator
                    p1 = p1.next
                    iterate = False

                elif iterator == None:
                    p2.next = None

            elif not iterate:
                iterator = iterator.next
                p2.next = iterator
                p2 = p2.next
                iterate = True

        p1.next = p2_head

        return head





    # Solved the problem correctly,
    # solved the wrong problem
    def oddEvenList2(self, head):

        if head == None:
            return head

        if head.val%2 == 0:
            p1 = None
            ans = None

        elif head.val%2 == 1:
            p1 = head
            ans = head

        if head.next == None:
            return head

        p2 = head.next
        p2_prev = head

        '''
        If the linked list starts with a node
        that has an even value, p1 = head
        else: p1 = None
        '''

        while p2 != None:
            # Is p2 odd or even?

            if p2.val%2 == 1:
                # odd

                if p1 == None:
                    # Start the list
                    '''
                    So p2 is odd. Now what?
                    p1 doesn't exist yet.
                    '''

                    p1 = ListNode(p2.val)
                    p1.next = head
                    ans = p1

                    p2 = p2.next
                    p2_prev.next = p2


                elif p1 != None:
                    # Update the list

                    tmp = ListNode(p2.val)
                    tmp.next = p1.next
                    p1.next = tmp
                    p1 = p1.next

                    p2 = p2.next
                    p2_prev.next = p2



            elif p2.val%2 == 0:
                # even
                p2_prev = p2
                p2 = p2.next


        return ans






    def oddEvenList1(self, head):
        if head == None:
            return head

        if head.val%2 == 0:
            p1 = None

        elif head.val%2 == 1:
            p1 = head

        if head.next == None:
            return head

        p2 = head.next
        p2_prev = head
        ans = None

        while True:
            if p2 != None:
                if p2.val%2 == 1:

                    print(p1.val)

                    if p1 == None:
                        print('hi')
                        # Assuming not mutable
                        # That we are making a
                        # copy of tmp and p2

                        # tmp = p2
                        tmp = ListNode(p2.val)
                        tmp.next = p2.next

                        # p2 = p2.next
                        tmp.next = head
                        p2_prev.next = p2.next
                        p1 = tmp
                        ans = tmp
                        p2 = p2.next


                        # print(p1.val)
                        # print(p2.val)

                    elif p1 != None:

                        # tmp = p2
                        tmp = ListNode(p2.val)
                        tmp.next = p2.next


                        tmp2 = p1.next
                        p1.next = tmp
                        p1.next.next = tmp2
                        p2_prev.next = p2.next

                elif p2.val%2 == 0:
                    p2_prev = p2
                    p2 = p2.next

            elif p2 == None:
                break

        return ans


if __name__ == '__main__':

    # 1->2->3->4->5->NULL
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(7)
    g = ListNode(8)


    head.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    # tmp = head
    # tmp.next = None
    #
    # print(head)



    # [1,2,3,4,5,6,7,8]


    print("Input: {}".format(str(head)))

    s = Solution()

    r = s.oddEvenList(head)

    print("Output: {}".format((r)))
