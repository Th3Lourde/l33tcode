# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Ok so we'd like to do a couple of things:
1) Figure out which nodes to reverse
2) Reverse them

Reversing a linked list is something we've done before
so let's focus on figuring out how to put bounds on the
reversing.

Let's have a start/stop node.
So a node to start the reversing at, and a node to stop
the reversing at.

Generate a node number to group mapping?

How about we create a group list

- Reverse all of the nodes in the even groups
- Point the last node in the even group to the first node
in the odd group, if possible
- Point the first node to the last node in the previous group

[5,6,2,3,9,1,4,8,3,7]
[5,6,2,3,9,1,4,8,3,7]
[5,6,2,3,9,1,4,8,3,7]
[1,0,1]
[1,0,1,6]
[2,1]
[2,1]
[8]

[0,4,2,1,3]
[0,2,4,3,1]

'''


class Solution:
    def reverseEvenLengthGroups(self, head):
        groupNumToNodes = []

        group = []
        currentGroup = 1
        node = head

        while node:
            # if node.next == None:
            #     groupNumToNodes.append(group)
            #     groupNumToNodes.append([node])
            #     group = []
            #     print("Breaking")
            #     break

            group.append(node)

            if len(group) == currentGroup:
                groupNumToNodes.append(group)
                group = list([])
                currentGroup += 1

            node = node.next


        if len(group) != 0:
            groupNumToNodes.append(group)

        # for group in groupNumToNodes:
        #     for group_node in group:
        #         print(group_node.val)
        #     print("|")


        # for idx in range(len(groupNumToNodes)):
        #     for group_idx in range(len(groupNumToNodes[idx])):
        #         print(groupNumToNodes[idx][group_idx].val)

        # print("Len Nodes: {}".format(len(groupNumToNodes)))
        # return


        def reverseList(head):
            if not head or not head.next:
                return head

            l = head
            m = head.next

            if not m.next:
                l.next = None
                m.next  = l
                return m

            r = m.next

            l.next = None
            m.next = l

            while r:
                tR = r.next
                r.next = m

                m = r
                r = tR

            return m

        for i in range(len(groupNumToNodes)):

            # Point last node to first node
            if len(groupNumToNodes[i]) % 2 == 0:
                groupNumToNodes[i-1][-1].next = None
                groupNumToNodes[i][-1].next = None
                reversed = reverseList(groupNumToNodes[i][0])

                tmp = []
                node = reversed

                while node:
                    tmp.append(node)
                    node = node.next

                groupNumToNodes[i] = tmp


                groupNumToNodes[i-1][-1].next = reversed

            else:
                if i > 0:
                    # # Find end of current node
                    # end = groupNumToNodes[i][0]
                    # recon = groupNumToNodes[i][0].next
                    #
                    # while recon:
                    #     end = end.next
                    #     recon = recon.next

                    groupNumToNodes[i-1][-1].next = groupNumToNodes[i][0]

        node = head

        # while node:
        #     print(node.val)
        #     node = node.next

        return head
