class Solution:
    def swapPairs(self, head):
        # 0,1 nodes in ll
        if not head or not head.next:
            return head

        # we know the length is 3
        if not head.next.next:
            c = head
            n = head.next

            n.next, c.next = c, None

        # 2 node swap b/c front
        c = head
        n = head.next
        resp = n

        # swap
        n.next, c.next = c, n.next
        # return resp

        # move to the next valid node to swap
        p = c
        c = c.next
        n = c.next

        while c and n:
            # 3 node swap
            p.next = n
            c.next = n.next
            n.next = c

            # re-position
            p = c
            c = c.next
            if c:
                n = c.next

        return resp
