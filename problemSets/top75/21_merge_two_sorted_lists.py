'''
Merge two sorted linked lists and return it as a
sorted list.

So basically two pointer method.
Go to next element.

If one element is gone but the other is there
add the rest of the list

1 --> 2 --> 4

1 --> 3 --> 4

Can either make a new list or can put one list onto the other

lets start with making a newList
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)


def makeLL(arr):
    head = ListNode(arr[0])
    node = head

    for idx in range(1, len(arr)):
        node.next = ListNode(arr[idx])
        node = node.next

    return head

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        n1 = l1
        n2 = l2

        head = None

        if n1.val <= n2.val:
            head = ListNode(n1.val)
            n1 = n1.next
        else:
            head = ListNode(n2.val)
            n2 = n2.next

        node = head

        while n1 and n2:
            if n1.val <= n2.val:
                node.next = ListNode(n1.val)
                n1 = n1.next

            else:
                node.next = ListNode(n2.val)
                n2 = n2.next

            node = node.next

        if not n1:
            node.next = n2

        if not n2:
            node.next = n1

        return head

print(Solution().mergeTwoLists(makeLL([4]), makeLL([1,3,4])))
print(Solution().mergeTwoLists(makeLL([2]), makeLL([1,3,4])))
print(Solution().mergeTwoLists(makeLL([1,1,1,1]), makeLL([1,3,4])))

'''
Works if left is None
Works if right is None
'''
