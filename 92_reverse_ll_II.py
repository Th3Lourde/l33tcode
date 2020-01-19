
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{}-->{}".format(self.val, self.next)


class Solution:
    def reverseBetween(self, head, m, n):

        if m == n:
            return head

        ans = head

        pos = 1
        itr = head

        if m == 1:
            start = None

        # While True?
        # while pos <= n+1:
        while True:

            if pos+1 < m:
                itr = itr.next
                pos += 1

                # set value for start
            elif pos+1 == m:
                start = itr
                itr = itr.next
                pos +=1

            # this node will either point
            # to None or n+1
            elif pos == m:
                past = itr
                last_n = itr
                itr = itr.next
                pos +=1
                past.next = None
                # print(last_n.next)

            elif m < pos and pos < n:
                current = itr
                itr = itr.next
                pos += 1

                # print(past)
                # print(current)
                current.next = past
                # print(current)
                past = current

            elif pos >= n:
                if itr.next == None:
                    last_n.next = None
                    itr.next = past

                    if start == None:
                        # m = 0; n = length of ll
                        return itr

                    elif start != None:
                        start.next = itr
                        return ans

                elif itr.next != None:
                    last_n.next = itr.next
                    itr.next = past

                    if start == None:
                        return itr

                    elif start != None:
                        start.next = itr
                        return ans


if __name__ == '__main__':

    s = Solution()

    tail = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)

    tail.next = a
    a.next = b
    b.next = c
    c.next = d

    print("start: {}".format(tail))

    tail = s.reverseBetween(tail, 4, 5)

    print("end: {}".format(tail))
