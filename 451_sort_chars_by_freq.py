'''
Given a string, sort it in decreasing order based on the frequency of characters.

Solution 1:
1) Get frequency of all characters
2) Put into heap/sorted list
3) Build a new string based upon the sorted frequency

'sseeef'
     ^
d = {'s': 2, 'e': 3, 'f': 1}

['s', 'e', 'f']

heap = [ [freq, char], ]

heap = [ [3, 'e'], [2, 's'], [1, 'f'] ]

 [3, 'e'] | [ [2, 's'], [1, 'f'] ]

 [2, 's'] | [ [1, 'f'] ]

 [1, 'f']

'''

import math

class Heap:
    def __init__(self):
        self.heap = []

    def add(self, x):
        # append to end
        # swim up
        self.heap.append(x)

        end = self.heap[-1]
        self.swim()

    def swim(self):

        if self.getSize() < 2: return

        i = self.getSize()-1

        parent = math.floor(i/2)

        while self.heap[parent] < self.heap[i]:
            self.swap(i, parent)

            i = parent
            parent = math.floor(i/2)

    def poll(self):
        # copy the first element
        # put the last element at the top
        # sink down

        if self.getSize() < 1: return

        elif self.getSize() == 1: return self.heap.pop()

        r = self.heap[0]

        self.heap[0] = self.heap.pop()

        # Maintain heap order

        top = self.heap[0]
        self.sink()

        while top != self.heap[0]:
            top = self.heap[0]
            self.sink()

        # print("\n[postPoll] {}\n".format(self.heap))

        return r

    def sink(self):

        # print("\n[preSink] {}".format(self.heap))

        if self.getSize() < 2: return

        i = 0
        l = 2*i + 1
        r = 2*i + 2

        while l < self.getSize() or r < self.getSize():

            if l < self.getSize() and self.heap[i][0] < self.heap[l][0]:

                self.swap(i, l)

                i = l
                l = 2*i + 1
                r = 2*i + 2

            elif r < self.getSize() and self.heap[i][0] < self.heap[r][0]:

                self.swap(i, r)

                i = r
                l = 2*i + 1
                r = 2*i + 2

            else:
                break

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def getSize(self):
        return len(self.heap)

    def __repr__(self):
        return "{}".format(self.heap)



class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i][0] > self.heapList[i // 2][0]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2



    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)


    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1




    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval


class Solution:
    def frequencySort(self, s):

        if len(s) < 2: return s

        d = {}

        for char in s:
            try:
                d[char] += 1

            except:
                d[char] = 1

        keys = list(d.keys())

        heap = BinHeap()

        for key in keys:
            heap.insert( [d[key], key] )

        ans = ""

        tmp = None

        while heap.currentSize > 0:

            top = heap.delMin()

            ans += top[1]*top[0]

        return ans



if __name__ == '__main__':
    s = Solution()


    testCases  =[
        # ["tree", "eert"],
        # ["cccaaa", "cccaaa"],
        # ["Aabb", "bbAa"],
        # [""]
        # ["dacca", "aaccd"]
        ["Mymommaalwayssaid,\"Lifewaslikeaboxofchocolates.Youneverknowwhatyou'regonnaget."]
    ]

    for tc in testCases:
        print(s.frequencySort(tc[0]))
