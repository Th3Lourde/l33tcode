
'''
My understanding is that I am to design a queue.
However this queue is of fixed length.
We can use a list to do this pretty easily.

[a,b] a represents the end of the queue, b represents the front of the queue.

if we dequeue, we get b
if we enqueue(0), we get [0,a,b]
We use k and the length of our list in order to judge if we can
perform the specified operation.
'''

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.queue = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """

        if self.k == len(self.queue):
            return False

        else:
            self.queue.append(value)
            return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """

        if self.k == len(self.queue):
            return False

        else:
            self.queue.insert(0, value)
            return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """

        if len(self.queue) == 0:
            return False

        else:
            self.queue.pop()
            return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """

        if len(self.queue) == 0:
            return False

        else:
            del self.queue[0]
            return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """

        if len(self.queue) == 0:
            return -1

        else:
            return self.queue[-1]


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """

        if len(self.queue) == 0:
            return -1

        else:
            return self.queue[0]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """

        return len(self.queue) == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """

        return len(self.queue) == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
