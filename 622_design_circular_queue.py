'''
k = 3 --> self.maxSize = 3, self.queue = []
enQueue(1) --> self.queue = [1]
enQueue(2) --> self.queue = [2,1]
enQueue(3) --> self.queue = [3,2,1]

#######################################################
# for [a,b,c], the 'front' is c and the 'back' is 'a' #
#######################################################

enQueue(x): insert at 0 index iff we have room
deQueue(x): pop() the list?
rear(): return [0] iff there, else -1
front(): return [-1] iff there, else -1
isEmpty(): return len(self.queue) == 0
isFull(): return len(self.queue) == self.k


'''
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxSize = k
        self.queue = []


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        elif not self.isFull():
            self.queue.insert(0, value)
            return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """

        if self.isEmpty():
            return False

        elif not self.isEmpty():
            self.queue.pop()
            return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """

        if len(self.queue) == 0:
            return -1

        else:
            return self.queue[-1]


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """

        if len(self.queue) == 0:
            return -1

        else:
            return self.queue[0]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """

        return len(self.queue) == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """

        return len(self.queue) == self.maxSize
