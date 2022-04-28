class Solution:
    def copyRandomList(self, head):
        if not head:
            return head

        valToNode = {}
        ptr = head

        # Populate valToNode
        while ptr:
            new_node = Node(ptr.val)
            valToNode[ptr] = new_node
            ptr = ptr.next

        ptr = head

        while ptr:
            if ptr.next != None:
                valToNode[ptr].next = valToNode[ptr.next]

            if ptr.random != None:
                valToNode[ptr].random = valToNode[ptr.random]

            ptr = ptr.next


        return valToNode[head]
