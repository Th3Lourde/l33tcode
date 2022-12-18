import random

class RandomizedSet:
    def __init__(self):
        self.n = 0
        self.direct = {}
        self.inverse = {}

    def insert(self, val):
        if val in self.direct:
            return False

        self.direct[val] = self.n
        self.inverse[self.n] = val
        self.n += 1
        return True

    def remove(self, val):
        if val not in self.direct:
            return False

        # Get ID of element we are deleting
        id = self.direct[val]

        # Get value of the last element
        replacement = self.inverse[self.n-1]

        self.direct[replacement] = id
        self.inverse[id] = replacement

        # delete what isn't needed
        del self.direct[val]
        del self.inverse[self.n-1]

        self.n -= 1
        return True


    def getRandom(self):
        id = random.randint(0,self.n-1)
        return self.inverse[id]


rs = RandomizedSet()

rs.direct
rs.inverse

rs.insert(4)
rs.insert(1)
rs.remove(1)
rs.remove(4)
