'''
So we have a set where we can:
insert 0(n),
remove 0(n),
and getRandom 0(n),

How do we do this?

Well sets are 0(n), however in order to get the elements, this would
require an 0(n) call to get all of the elements.

So are there any data structures that are 0(1) for add/delete?
sets
dictionarys
linkedList?

What if we have a doubly linked list with a hashtable lookup?
We could also have a head, tail, and a ptr to a random node.
Every time we getRandom we can do .next. And then set to head.

numToNode = {

}

head
random

on insert:
- if element in numToNode, return false
- add to end of linkedList
- if creating the list for the first time, set rand to this node

remove:
- if element not in numToNode, return false
- remove from linkedList, if random is this element,
get the next/prev (if such a node exists)

getRandom:
- move forwards one (set to head if .next == None)
- return node
'''

class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

class RandomizedSet:
    def __init__(self):
        self.valToNode = {}
        self.head = None
        self.tail = None
        self.ran = None

    def insert(self, val):
        # Check if val already exists
        if val in self.valToNode:
            return False

        node = ListNode(val)
        self.valToNode[val] = node

        # LL is empty
        # LL is not empty
        if not self.head:
            self.head = node
            self.tail = node
            self.ran = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        return True

    def remove(self, val):
        # Check if val in dict
        if val not in self.valToNode:
            return False

        # Check if val is ran
        if self.ran == self.valToNode[val]:
            self.getRandom()

        # Delete current element
        # If there is only on element in the list
        if self.head == self.tail:
            self.valToNode = {}
            self.head = None
            self.tail = None
            self.ran = None
        else:
            # If there are other elements in the list
            node = self.valToNode[val]

            if self.head == node:
                self.head = self.head.next
                self.head.prev = None

            elif self.tail == node:
                self.tail = self.tail.prev
                self.tail.next = None

            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            del self.valToNode[val]

        return True

    def getRandom(self):
        resp = self.ran
        
        if self.ran.next:
            self.ran = self.ran.next
        else:
            self.ran = self.head

        return resp.val


rs = RandomizedSet()

rs.insert(1)
rs.insert(2)
rs.insert(3)
rs.insert(4)

rs.remove(2)

rs.getRandom()

rs.head
