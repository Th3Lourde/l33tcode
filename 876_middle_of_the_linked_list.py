
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

'''
The first thing that we have to do
is figure out how large the linked
list is.

We are assuming that the linked list
does not have a cycle in it.

We want to know how many times we need
to do .next.

1 2 3

Or just get length, // 2, then for i in range, .next


'''




class Solution:
    def middleNode(self, head):
        n = 1

        node = head

        while node:
            node = node.next
            n += 1

        n -= 1

        # print(n)

        node = head

        for i in range(n//2):
            node = node.next

        return node


if __name__ == '__main__':
    s = Solution()

    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    one.next = two
    two.next = three
    three.next = four
    four.next = five

    # print(one)

    print(s.middleNode(five))
