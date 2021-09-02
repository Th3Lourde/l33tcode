'''
Solution 1:
Store the memory address of each node
in a hashmap, if we see a repeat, return True

Solution 2:
Update the data-type to be something that a
ll would never have (string or -inf). If we
see that value we know we are seeing an element
that we have already seen

Solution 3:
Fast/Slow pointer. If fast ever equals slow,
return True.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}-->{}".format(self.val, self.next)

def makeLLWCycle(arr, n):
    head = ListNode(arr[0])
    d = {0: head}
    node = head

    for idx in range(1, len(arr)):
        node.next = ListNode(arr[idx])
        node = node.next
        d[idx] = node

    if n != -1:
        d[len(arr)-1].next = d[n]

    return head

class Solution:
    def hasCycle_1(self, head):
        d = {}
        node = head

        while node:
            if node not in d:
                d[node] = True

            else:
                return True

            node = node.next

        return False

    def hasCycle_2(self, head):
        node = head

        while node:
            if type(node.val) == str:
                return True

            node.val = str(node.val)
            node = node.next

        return False

    def hasCycle(self, head):
        fast = head
        slow = head

        while fast and slow:
            fast = fast.next
            slow = slow.next

            if fast:
                fast = fast.next

                if fast == slow:
                    return True

        return False

print(Solution().hasCycle(makeLLWCycle([1,2,3], 0)))
print(Solution().hasCycle(makeLLWCycle([1,2,3], -1)))
print(Solution().hasCycle(makeLLWCycle([1,2,3], 1)))
