'''
Ok this problem is tough, the linear solution
comes from an academic paper.

Let's just use a heap and get on with it.

Put in the elements 0(n), pop until target, 0(k),
worst-case 0(n²).

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
            if self.heapList[i] < self.heapList[j]:
                return True

            else:
                return False

        elif self.type == "max":
            if self.heapList[i] > self.heapList[j]:
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


class Solution:

    def kthSmallest(self, matrix, k):
        q = priorityQueue("min")

        column_vector = []

        for row in matrix:
            for element in row:
                column_vector.append(element)

        q.buildHeap(column_vector)

        for i in range(k):
            ans = q.poll()

        return ans


        # Same story
    def kthSmallest_2(self, matrix, k):
        if k == 1:
            return matrix[0][0]

        n = len(matrix)

            # n is the len of the matrix
            # we are at the value matrix[k][k]
        def getElementNum(n, k):
            if k == 1: return 1

            top = (k-1)*n
            bottom = (k-1)*(n-k+1)

            return top + bottom + 1

        l = -1
        r = n

        while l < r:
            tmp = (l+r) // 2
            mid = getElementNum(n, tmp)

            print("At tmp: {}".format(tmp))

            if mid == k:
                return matrix[tmp-1][tmp-1]

            elif mid < k:
                l = l + tmp

            elif mid > k:
                r = tmp

        print("mid: {} | l: {} | r: {}".format(mid, l, r))

        if getElementNum(n, l) > k:
            l = max(0, l-1)

        # At right edge location find the term

        row = col = l-1
        smallest = getElementNum(n, l)

        print("Starting at idx [{}][{}] = {}".format(row, col, smallest))

        row += 1

        while row < n:
            a = min(matrix[row][col], matrix[col][row])
            b = max(matrix[row][col], matrix[col][row])
            print("a: {}".format(a))
            print("b: {}".format(b))

            if smallest + 1 == k:
                return a

            elif smallest + 2 == k:
                return b

            smallest += 2
            row += 1


        # Solves the wrong problem.
    def kthSmallest_1(self, matrix, k):
        n = len(matrix)

        col = k % n

        if col == 0:
            col = n

        row = (k-1) // n

        return matrix[row][col-1]

if __name__ == '__main__':
    s = Solution()

    m = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
        ]


    # print(s.kthSmallest(m, 2))

    for i in range(1, 10):
        print("{}th smallest element is: {}".format(i,s.kthSmallest(m, i)))
