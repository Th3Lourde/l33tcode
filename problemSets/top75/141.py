'''
Ok there is some proof that if you have a fast and
slow pointer, that they will at one point hit each other.

Let's see if we can't find some of the intuition behind this:

If there isn't a cycle, then one of the pointers will just become
null.

If there is a cycle, then, since one pointer is always going one faster than the other,
if will eventually catch up.

3 --> 2 --> 0 --> -4 -->2
                  p1
                  p2

'''

class Solution:
    def hasCycle(self, head):
        if not head:
            return False

        p1 = head
        p2 = head

        while p1 and p2:
            p1 = p1.next
            p2 = p2.next

            if p2:
                p2 = p2.next
            else:
                return False

            if p1 == p2:
                return True

        return False
