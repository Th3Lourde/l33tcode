'''



'''


class MedianFinder:
    def __init__(self):
        self.l = []
        self.lenL = 0
        self.m = None

    def binary_search(self, targ):
        l, r = 0, len(self.l)-1

        while l < r:
            m = (l+r)//2

            if self.l[m] >= targ:
                r = m
            else:
                l = m+1

        return l


    def addNum(self, num):
        # Add to list, mantain order
        if self.l == []:
            self.l = [num]
        elif num < self.l[0]:
            self.l = [num] + self.l
        elif num > self.l[-1]:
            self.l.append(num)
        else:
            self.l.insert(self.binary_search(num), num)

        self.lenL += 1

        # Store median
        if self.lenL % 2 == 0:
            ave = (self.l[(self.lenL//2) - 1] + self.l[self.lenL//2])/2
            self.m = ave
        else:
            self.m = self.l[self.lenL // 2]


    def findMedian(self):
        return self.m


if __name__ == '__main__':
    m = MedianFinder()

    inp = [4,3,2,3,5,6,4,3,1,2,4,5,7,5,3]

    for e in inp:
        m.addNum(e)
        print("After adding {}, median: {}, l: {}, arr: {}".format(e, m.findMedian(), m.lenL, m.l))
