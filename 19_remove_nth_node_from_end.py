
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Ok so remove nth node from the end

So remove the len(linkedlist)-n node (going left to right)

1 → 2 → 3 → 4 → 5

Use a stack to iterate through the list, once at the end,
pop k+1 times. k.next = (k+2).

So store two values, k, k+1

Iterate through linked list once, store nodes in a stack.

[1,2,3,4,5]
       ^

k = 1, Just remove the last element
k != 1,

pop k+1 times, use next to get the answer.

we know that a solution will exist b/c k != 1.




'''

class Solution:
    # Redoing the problem
    # TC: Worst Case O(n²) | O(n+k), k == inputted n
    # SC: O(n)
    def removeNthFromEnd(self, head, n):
        s = []
        node = head

        while node:
            s.append(node)
            node = node.next

        for i in range(n+1):
            node = s.pop()

        if len(s) == 1:
            return None
        elif len(s) == n:
            return head.next 

        if n == 1:
            node.next = None
        else:
            node.next = node.next.next

        return head

    # two-pass solution
    # run-time: O(n^2)
    # memory complexity: O(1)
    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        len = 0
        node = head

        while node:
            len += 1
            node = node.next

        target = len-n

        if target == 0:
            return head.next

        tmp = 0
        node = head

        while tmp < target-1: # get to node before target
            node = node.next
            tmp += 1

        if n == 1:
            node.next = None
            return head

        elif n != 1:
            tmp = node
            node =  node.next.next
            tmp.next = node
            return head

    # run-time: O(n)
    # memory complexity: O(n)
    def removeNthFromEnd_1(self, head: ListNode, n: int) -> ListNode:
        node = head
        llnodes = []

        while node:
            llnodes.append(node)
            node = node.next

        target = len(llnodes) - n

        if target == 0:
            return head.next

        elif target == len(llnodes)-1:
            llnodes[-2].next = None
            return head

        elif 0 < target and target < len(llnodes)-1:
            llnodes[target-1].next = llnodes[target+1]
            return head



if __name__ == '__main__':
    s = Solution()
