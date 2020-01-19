


class MyLinkedList:

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

    LL = MyOtherLinkedList()

    for i in range(5,0,-1):
        LL.addAtHead(i)

    print(LL)

    """
    ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    """
