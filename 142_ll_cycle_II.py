
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Given linked list, return the node where the
cycle begins. If there is no cycle, return None.

Return the idx where the cycle exists. (Start at 0)

Solution 1: Store the memory addresses of each node, when
we find a repeat, return that node.

Worst Case:
    TC: 0(n²)
    SP: 0(n)

Solution 2:

Ok so I was correct in the idea that the one and two don't
tell us anything except that a cycle exists.

1 --> 2 --> 3 --> 4 --> 5 --> 3
                        t
                        h
            c

            t

Want to return 2 (the node 3)

Ok so this is an algo that I don't really understand but I now know.







'''

class Solution:

        # Optimal Solution
        # 0(n + ( n - k ) )
    def detectCycle(self, head):
        # 1) Detect if there is a cycle
        if not head: return None

        a = head
        b = head
        isCycle = False

        while b:
            a = a.next

            b = b.next
            if b:
                b = b.next
            else:
                return None

            if a == b:
                isCycle = True
                break
        if not b: return None

        # 2) Find it

        while head != b:
            head = head.next
            b = b.next

        return head


    def detectCycle_2(self, head):
        s = set()
        node = head

        while node:

            if node not in s:
                s.add(node)

            else:
                return node

            node = node.next

        return None


        # Works?
    def detectCycle_1(self, head):
        if head == None or head.next == None:
            return None

        head.val = str(head.val)

        if type(head.next) == str:
            headv.val = int(head.val)
            return head

        tmp = head
        headv = head.next

        while True:
            if type(headv.val) == str:
                # tmp.val = int(tmp.val)
                # return tmp

                headv.val = int(headv.val)
                return headv
            elif type(headv.val) == int:
                headv.val = str(headv.val)
                if  headv.next == None:
                    return None
                elif headv.next != None:
                    tmp = headv
                    headv = headv.next

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    s = Solution()


    r = s.detectCycle(a)
    print(r.val)
