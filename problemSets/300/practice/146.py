class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return "({},{})-->{}".format(self.key, self.val, self.next)

class LRUCache:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.dict = {}
        self.capacity = capacity

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            # print(self.head)
            self.delFromLL(node)
            # print(self.head)
            self.insertToFront(node)
            # print(self.head)
            return node.val

        return -1

    def put(self, key, val):
        if key in self.dict:
            node = self.dict[key]
            self.delFromLL(node)
            self.insertToFront(node)
            node.val = val
        else:
            if len(self.dict) >= self.capacity:
                if self.tail.key in self.dict:
                    del self.dict[self.tail.key]

                self.delFromLL(self.tail)

            node = ListNode(key, val)
            self.insertToFront(node)
            self.dict[key] = node


    def delFromLL(self, node):
        if not node:
            return

        if not node.next and not node.prev:
            # print("A")
            # 0
            self.head = None
            self.tail = None

        elif node.prev and node.next:
            # print("B")
            node.prev.next = node.next
            node.next.prev = node.prev
            # 0 --> 1 --> 2
            # 0 <-- 1 <-- 2
            # 0    -->       2
            # 0    <--     2

        elif not node.prev:
            # print("C")
            # 0 --> 1 --> 2
            #       ^
            self.head = node.next
            self.head.prev = None

        elif not node.next:
            # print("D")
            # 0 --> 1  2
            #       ^

            self.tail = node.prev
            self.tail.next = None

        node.next = None
        node.prev = None

    def insertToFront(self, node):
        # Opt1: No list
        # Opt1: There is a head

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def createNode(self, key, val):
        return ListNode(key, val)

c = LRUCache(2)

c.put(1,1)
c.put(2,2)
c.get(1)
c.get(1)

c.head
c.tail
c.dict


'''
d: {
    1: (1,1)
    2: (2,2)

}

ll:
(2,2) --> (1,1)

'''

c.put(1,1)
c.put(2,2)
c.put(3,3)
c.put(2,4)
c.put(2,4)
c.put(2,4)
c.get(4)
c.get(2)
c.put(3,3)
c.get(1)

c.head
c.tail
c.dict
