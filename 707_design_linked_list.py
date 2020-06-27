class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.currentSize = 0

    def __repr__(self):
        return "{}".format(str(self.head))


    def get(self, index: int, wantNode=False) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        # print("index: {} currentSize: {}".format(index, self.currentSize))

        if index >= self.currentSize or index < 0:
            return -1

        mid = (self.currentSize-1) // 2

        if index > mid:
            # start from tail
            i = self.currentSize-1
            node = self.tail

            while i > index:
                node = node.prev
                i -= 1


        elif index <= mid:
            # start from head
            i = 0
            node = self.head

            while i < index:
                node = node.next
                i += 1

        if wantNode:
            return node

        return node.val


        # Do the math to figure out if we start from tail or head

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        if self.currentSize == 0:
            self.head = self.tail = ListNode(val)


        elif self.currentSize > 0:
            node = ListNode(val)
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.currentSize += 1

        # print(self.currentSize)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        if self.currentSize == 0:
            self.head = self.tail = ListNode(val)

        elif self.currentSize > 0:
            node = ListNode(val)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.currentSize += 1

        # print(self.currentSize)



    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index < 0:
            print("Index Invalid")

        if index == 0:
            self.addAtHead(val)
            print("hi")
            return

        if index >= self.currentSize:
            self.addAtTail(val)
            return


        node = self.get(index, wantNode=True)
        tmp = ListNode(val)


        if node.prev and node.next:
            node.prev.next = tmp
            tmp.prev = node.prev
            node.prev = tmp
            tmp.next = node

        elif node.next:
            tmp.next = node
            node.prev = tmp
            self.head = tmp

        elif node.prev:
            node.prev.next = tmp
            tmp.prev = node.prev
            tmp.next = node
            node.prev = tmp
            self.tail = tmp.next


        # tmp = ListNode(val)
        # tmp.prev = node.prev
        # node.prev.next = tmp
        # node.prev = tmp
        # tmp.next = tmp

        self.currentSize += 1

        # print(self.currentSize)



    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.currentSize:
            return "Index Invalid"

        node = self.get(index, wantNode=True)

        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        elif node.prev:
            node.prev.next = None
            self.tail = node.prev

        elif node.next:
            node.next.prev = None
            self.head = node.next

        self.currentSize -= 1




class MyLinkedListWorks: # first implementation that works

    def __init__(self):

        """
        Initialize your data structure here.
        """

        self.data = []

        # print("Init: {}".format(self.data))


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """

        if index > len(self.data)-1:
            # print("[failed] Get {}: {}".format(index, self.data))
            return -1

        elif index <= len(self.data)-1:
            # print("Get {}: {}".format(index, self.data))
            return self.data[index]


    def addAtHead(self, val: int) -> None:
        """
        Add a node of the value val before the first nums[i] of the linked
        list. After the insertion, the new node will be the first node of
        the linked list.
        """

        self.data.insert(0, val)

        # print("addAtHead {}: {}".format(val, self.data))


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last nums[i] of the linked list.
        """

        self.data.append(val)

        # print("addAtTail {}: {}".format(val, self.data))


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of the value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.

        * Assuming that the index >= 0
        """

        if index <= len(self.data):
            self.data.insert(index, val)

            # print("addAtIndex[{}] {}: {}".format(index, val, self.data))

        elif index > len(self.data):
            return None
            # print("[failed] addAtIndex[{}] {}: {}".format(index, val, self.data))


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        try:
            self.data[index]
            del self.data[index]
            # print("deleteAtIndex {}: {}".format(index, self.data))

        except:
            return None
            # print("[failed] deleteAtIndex {}: {}".format(index, self.data))





class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return "{} --> {}".format(self.val, self.next)

# Implemented with a node class
# Singly Linked List
class MyOtherLinkedList:

    def __init__(self):

        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if index > self.length-1:
            return -1

        elif index <= self.length-1:
            """
            if 3, return the 3rd node, index 2
            move right index-1 (-1 since we start at head)

            1 --> 2 --> 3 --> 4
            get(2) returns 3
            """
            tmp = self.head

            for i in range(index):
                tmp = tmp.next

            return tmp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of the value val before the first nums[i] of the linked
        list. After the insertion, the new node will be the first node of
        the linked list.
        """
        if self.head.val == None:
            self.head.val = val

        elif self.head.val != None:
            tmp = Node(val)
            tmp.next = self.head
            self.head = tmp

        self.length += 1

        print(str(self.head) + " length: {}".format(self.length))

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last nums[i] of the linked list.
        """

        if self.head.val != None:
            if self.head == self.tail:
                self.head.next = Node(val)
                self.tail = self.head.next

            elif self.head != self.tail:
                self.tail.next = Node(val)
                self.tail = self.tail.next

        elif self.head.val == None:
            self.head.val = val

        self.length += 1

        print(str(self.head) + " length: {}".format(self.length))

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a Node of the value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.

        * Assuming that the index >= 0
        """

        if index > self.length:
            return None

        elif index == 0:
            self.addAtHead(val)

        elif index == self.length:
            self.addAtTail(val)

        elif (index < self.length) and (index > 0):
            tmp = self.head

            for i in range(index-1):
                tmp = tmp.next

            tmp2 = tmp.next
            tmp.next = Node(val)
            tmp.next.next = tmp2

            self.length += 1

        print(str(self.head) + " length: {}".format(self.length))

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index > self.length-1:
            return -1

        else:

            if index == 0:
                self.head = self.head.next

            elif index == self.length-1:
                tmp = self.head
                for i in range(self.length-2):
                    tmp = tmp.next

                self.tail = tmp
                self.tail.next = None

            elif index > 0 and index < self.length-1:
                tmp = self.head

                for i in range(index-1):
                    tmp = tmp.next

                tmp2 = tmp.next.next

                tmp.next = tmp2

            self.length -= 1

        print(str(self.head) + " length: {}".format(self.length))

    def __str__(self):
        return str(self.head)


if __name__ == '__main__':

    ll = MyLinkedList()

    ll.addAtIndex(0,10)
    ll.addAtIndex(0,20)
    ll.addAtIndex(1,30)

    ll.get(0)

    # ll.addAtHead(10)
    # ll.addAtHead(20)


    ll

    """
    Test cases:
    """

    """
["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    """

    """
["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
[[],[0,10],[0,20],[1,30],[0]]
    """
