'''
Design a hashSet without using any
built-in hash table libraries

I'm assuming that we can't use a dict
and that we can't use a set.

So let's use an arr

Let's have an empty array.

Each insertion will take 0(n) time.

Perform binary search on the array. If
the element dne, add it.

Keep a sorted array of all of the elements that
we have seen thus far.

Or

Initialize an array of size 10^6 and represent if
the number is there using t/f.
 0 1 2 3 4 5 6
[0,1,2,3,4,5,6]
       l
       r

t = 3
'''

class MyHashSet:
    def __init__(self):
        self.arr = []

    def add(self, key):
        if len(self.arr) == 0:
            self.arr.append(key)
        elif self.contains(key):
            return
        else:
            l = 0
            r = len(self.arr)-1

            while l < r:
                m = (l+r)//2

                if self.arr[m] >= key:
                    r = m

                else:
                    l = m+1

            if self.arr[l] > key:
                self.arr.insert(l, key)
            else:
                self.arr.insert(l+1, key)

    def remove(self, key):
        if len(self.arr) == 0:
            return

        l = 0
        r = len(self.arr)-1

        while l < r:
            m = (l+r)//2

            if self.arr[m] >= key:
                r = m

            else:
                l = m+1

        if self.arr[l] == key:
            del self.arr[l]

    def contains(self, key):
        if len(self.arr) == 0:
            return False

        l = 0
        r = len(self.arr)-1

        while l < r:
            m = (l+r)//2

            if self.arr[m] >= key:
                r = m

            else:
                l = m+1

        return self.arr[l] == key

hs = MyHashSet()

hs.arr

hs.remove(2)

hs.add(3)
hs.add(1)
hs.add(2)
hs.contains(1)
hs.contains(3)
hs.add(2)
hs.contains(2)
hs.remove(2)
hs.contains(2)
