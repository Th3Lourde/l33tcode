'''
Throw everything into heap
Have custom heap so we compare the .val
of an element for our shouldSwap

# Loop through all of the ll's, throw
them all into the heap

while the heap is not empty
poll from heap
add that node to our 'answer'

if node.next:
    minPQ.insert(node.next)

[1,2,3,4]
 ^
'''

class priorityQueue:
    def __init__(self, t):

        if type(t) != type('s') or t != "max" and t != "min":
            return "Invalid Type"

        self.heapList = [0]
        self.currentSize = 0
        self.type = t

    def __repr__(self):
        return "{}".format(self.heapList)

    def getType(self):
        return self.type

    def size(self):
        return self.currentSize

    def buildHeap(self, alist):
        '''
        i = index of the last parent
        perform on perc down on all parents
        '''

        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        i = len(alist) // 2
        while (i > 0):
            self.percDown(i)
            i = i - 1

        # If j is i's parent, would swapping
        # cause the heap order to hold?
    def shouldSwap(self, i, j):
        if self.type == "min":
            if self.heapList[i].val < self.heapList[j].val:
                return True

            else:
                return False

        elif self.type == "max":
            if self.heapList[i].val > self.heapList[j].val:
                return True

            else:
                return False

    def percUp(self, i):
        while i // 2 > 0:
          if self.shouldSwap(i, i // 2):
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        # Touches all nodes with children
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.shouldSwap(mc, i):
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.shouldSwap(i*2, i*2+1):
                return i * 2
            else:
                return i * 2 + 1

    def poll(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def peekTop(self):
        if self.size() > 0:
            return self.heapList[1]

        else:
            raise Exception('Heap is empty')

class Solution:
    def mergeKLists(self, lists):


        for i in range(len(lists)-1, -1, -1):
            if not lists[i]:
                del lists[i]

        if not lists: return None

        minPQ = priorityQueue('min')
        minPQ.buildHeap(lists)

        ans = ListNode(None)
        ptr = ans

        while minPQ.size() > 0:
            node = minPQ.poll()

            if node.next:
                minPQ.insert(node.next)
                node.next = None

            ptr.next = node
            ptr = ptr.next

        return ans.next
