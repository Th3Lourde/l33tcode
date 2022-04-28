class Solution:
    def insertionSortList(self, head):
        nodes = []
        node = head

        while node:
            nodes.append(node)
            node = node.next

        ptr = 1

        while ptr < len(nodes):
            if nodes[ptr].val > nodes[ptr-1].val:
                lPtr = ptr-1

                while lPtr > 0 and nodes[lPtr].val > nodes[ptr].val:
                    lPtr -= 1

                nodes.insert(lPtr, nodes[ptr])
                del nodes[ptr]

            ptr += 1

        for node in nodes:
            print(node.val)

        for idx in range(len(nodes)-1):
            nodes[idx].next = nodes[idx+1]

        nodes[-1].next = None

        return nodes[0]
