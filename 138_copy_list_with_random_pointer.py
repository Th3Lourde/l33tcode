class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        return "{} {}".format(self.val, self.next)

class Solution:

    def copyRandomList(self, head):

        if not head:
            return None

        d = {}
        count = 0
        node = head
        ans = Node(head.val, None, None)
        d[count] = ans
        count += 1
        tmp = node
        node = node.next

        while node:
            ans.next = Node(node.val, None, None)
            d[tmp] = ans
            count += 1
            node = node.next
            ans = ans.next
            tmp = tmp.next

        d[tmp] = ans

        # Have copied LL (not yet random index)

        ans = d[0]
        node = head

        while ans:
            try:
                ans.random = d[node.random]
            except:
                ans.random = None

            node = head
            ans = ans.next
            node = node.next


        return d[0]

    # Guess I already did this...
    def copyRandomList_1(self, head):

        if head == None:
            return head

        tmp = head

        head2 = Node(tmp.val, -1, -1)
        tmp2 = head2

        tmp = tmp.next

        while tmp != None:
            tmp2.next = Node(tmp.val, -1, -1)
            tmp2 = tmp2.next
            tmp = tmp.next

        tmp2.next = None


        print(head)
        print(head2)

        '''
        Now we do the random
        '''



if __name__ == "__main__":
    s = Solution()

    h = Node(1,-1,-1)
    a = Node(2,-1,-1)
    b = Node(3,-1,-1)
    c = Node(4,None,-1)

    h.next = a
    a.next = b
    b.next = c

    s.copyRandomList(h)
