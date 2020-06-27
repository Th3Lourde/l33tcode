'''
add value to hashset
we only care about whether or
not the key exists, there is
no value associated with it.

Literally same problem, only
our elements are integers and
not lists.
'''


class MyHashSet: # Works

    def __init__(self):
        self.hashSet = [[] for i in range(10000)]

    def add(self, key):

        if self.contains(key) == True: return

        index = key % 10000

        self.hashSet[index].append(key)

    def remove(self, key):

        if self.contains(key) == False: return

        index = key % 10000

        z = 0

        while z < len(self.hashSet[index]) and self.hashSet[index][z] != key:
            z += 1

        del self.hashSet[index][z]

    def contains(self, key): # bool
        index = key % 10000

        if self.hashSet[index] == []: return False

        z = 0

        while z < len(self.hashSet[index]) and self.hashSet[index][z] != key:
            z += 1

        if z >= len(self.hashSet[index]):
            return False

        return True


if __name__ == '__main__':
    hs = MyHashSet()

    hs.remove(3)

    hs.add(3)

    hs.contains(3)
