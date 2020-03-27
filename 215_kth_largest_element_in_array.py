
class Heap:
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self, val):
        self.data.append(val)
        childIndex = len(self.data)-1
        self.size += 1

        while True:
            parentIndex = childIndex//2

            if self.data[parentIndex] < self.data[childIndex]:
                tmp = self.data[parentIndex]
                self.data[parentIndex] = self.data[childIndex]
                self.data[childIndex] = tmp

                childIndex = parentIndex

            else:
                break

    def pop(self):
        ans = self.data[0]

        if self.size == 1:
            self.data = []
            return ans

        self.data[0] = self.data.pop()
        parentIndex = 0
        self.size -= 1

        while self.size > 0:
            children = []

            if parentIndex == 0:
                if self.size == 2:
                    children = [1]
                elif self.size >= 3:
                    children = [1,2]

            elif parentIndex != 0:
                if parentIndex*2+1 <= self.size-1:
                    children.append(parentIndex*2+1)

                if parentIndex*2 <= self.size-1:
                    children.append(parentIndex*2)

            if children == []:
                return ans

            elif len(children) == 1:

                if self.data[parentIndex] < self.data[children[0]]:
                    tmp = self.data[parentIndex]
                    self.data[parentIndex] = self.data[children[0]]
                    self.data[children[0]] = tmp

                    parentIndex = children[0]

                else:
                    return ans

            elif len(children) == 2:

                if self.data[children[0]] >= self.data[children[1]] and self.data[parentIndex] < self.data[children[0]]:
                    tmp = self.data[parentIndex]
                    self.data[parentIndex] = self.data[children[0]]
                    self.data[children[0]] = tmp

                    parentIndex = children[0]

                elif self.data[children[0]] < self.data[children[1]] and self.data[parentIndex] < self.data[children[1]]:
                    tmp = self.data[parentIndex]
                    self.data[parentIndex] = self.data[children[1]]
                    self.data[children[1]] = tmp

                    parentIndex = children[1]

                else:
                    return ans

    def peak(self):
        return self.data[0]

    def __str__(self):
        return "{}".format(self.data)


class Solution:
    def findKthLargest(self, nums, k):
        heap = Heap()

        for num in nums:
            heap.insert(num)

        for i in range(k):
            ans = heap.pop()

        return ans




if __name__ == '__main__':

    # h = Heap()
    # h.insert(3)
    # h.insert(1)
    # h.insert(1)
    # h.insert(1)
    # h.insert(1)
    # h.insert(2)
    # h.insert(5)
    # print(h)
    # print(h.pop())
    # print(h)
    # print(h.pop())
    # print(h)
    # print(h.pop())
    # print(h)

    s = Solution()

    testCases = [
        [[3,2,1,5,6,4], 2, 5],
        [[3,2,3,1,2,4,5,5,6],4 , 4],
        [[2,1], 1, 2]
    ]

    z = 1
    for test in testCases:
        resp = s.findKthLargest(test[0], test[1])

        if resp == test[2]:
            print("[test case {} passed]".format(z))

        elif resp != test[2]:
            print("[test case {} failed]".format(z))

        z += 1
