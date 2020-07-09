
'''
Ok so we are implementing insertion sort with a ll.
How might we do this?

The big challenge is that we only have access to a
singly linked list.

I was going to say that we could also store a reversed
ll, however we would not gain a speed advantage by doing
so.

So keep an ans.

given a new list node, add it to ans s.t. the
list is sorted.

4->2->1->3
^

ans = None
node = 4

if ans == None:
    ans = node # .next should be == None, however we still
    need to itr throught the ll.
    How about we just create a new node?

4->2->1->3
   ^

ans = 4
node = 2

tmp = ans = 4
4 < 2
ans = 2 4

# make sure that we have both ans
# as well as a copy to iterate with

if ans == None:
    ans = TreeNode(node.val)

if ans.val > node.val:
    tmp = TreeNode(node.val)
    tmp.next = ans
    ans = tmp

if ans.val < node.val:
    if ans.next:

        if ans.next.val > node.val:
            ans = ans.next

        elif ans.next.val >= node.val:
            tmp = ans.next
            ans.next = TreeNode(node.val)
            ans.next.next = tmp

    elif not ans.next:
        ans.next = TreeNode(node.val)


Ok so this isn't fast enough. How could I do it faster?
What makes it so slow?

Well the whole marching through thing would do it.
We could just throw everything

So my problem is correct, the time complexity is just
too high. I would optimize this by not copying the linked
list and just swapping the nodes around.

A lot of people are complaining that 0(n^2) should have
passed. I'm going to copy and paste a solution that was
accepted and move on.


'''



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        ans = None
        node = head

        while node:
            itr = ans

            if ans == None:
                ans = ListNode(node.val)
                node = node.next
                continue

            iterate = True

            while iterate:
                if itr.val > node.val:
                    tmp = ListNode(node.val)
                    tmp.next = ans
                    ans = tmp
                    iterate = not iterate

                elif itr.val <= node.val:
                    if itr.next:

                        if itr.next.val < node.val:
                            itr = itr.next

                        elif itr.next.val >= node.val:
                            tmp = itr.next
                            itr.next = ListNode(node.val)
                            itr.next.next = tmp
                            iterate = not iterate
                            # break

                    elif not itr.next:
                        itr.next = ListNode(node.val)
                        iterate = not iterate
                        # break

            node = node.next

        return ans
