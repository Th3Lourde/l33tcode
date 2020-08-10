'''



'''


# Works, isn't as fast as it could be
class Solution:
    def getHappyString(self, n, k):

        class charHeap:
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

            def shouldSwap(self, i, j):
                if self.type == "min":
                    if self.heapList[i] < self.heapList[j]:
                        return True

                    return False

                elif self.type == "max":
                    if self.heapList[i] > self.heapList[j]:
                        return True

                    return False


                # If j is i's parent, would swapping
                # cause the heap order to hold?

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
                    # if self.heapList[i*2] < self.heapList[i*2+1]:
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

        c_to_opt = {
            "a": ["b","c"],
            "b": ["a","c"],
            "c": ["a","b"],
        }

        happyHeap = charHeap("min")

            # len(h) != 0
        def itr_happy(h):
            if len(h) == n:
                happyHeap.insert(h)

            elif len(h) != n:
                chr = h[-1]

                for o in c_to_opt[chr]:
                    tmp = str(h)+o
                    itr_happy(tmp)

        for chr in ["a","b","c"]:
            itr_happy(chr)

        if happyHeap.size() < k:
            return ""

        for i in range(k-1):
            happyHeap.poll()

        return happyHeap.poll()


if __name__ == '__main__':
    s = Solution()

    print(s.getHappyString(1, 3))
    print(s.getHappyString(3, 9))
