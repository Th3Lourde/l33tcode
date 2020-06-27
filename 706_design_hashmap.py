'''
1 million unique values
I'm just going to mod them.

It depends how much memory I can use.

So let's use z_10000

Means we need an array of size 10000

Given a key, we convert the key: key % 10000.
Do this conversion, search the corresponding
index for our value. If we find it, update
the val.

If we don't find it, pop()

For get, just return the value if found, else
return -1

For remove: if len() == 1, just set the key = []
Else, del[i].

'''

class MyHashMap: # Works

    def __init__(self):
        self.hashMap = [ [] for i in range(10000) ]

    def put(self, key, value):
        index = key % 10000

        # initialize the value if list is empty
        if self.hashMap[index] == []:
            self.hashMap[index].append([key, value])

            # search for the value. If we find it, update the val
            # If we don't append it.
        else:
            z = 0

            while z < len(self.hashMap[index]) and self.hashMap[index][z][0] != key:
                z += 1

            if z < len(self.hashMap[index]) and self.hashMap[index][z][0] == key:
                self.hashMap[index][z][1] = value

            else:
                self.hashMap[index].append([key, value])

    def get(self, key):
        index = key % 10000

        if self.hashMap[index] == []:
            return -1

        else:
            z = 0

            while z < len(self.hashMap[index]) and self.hashMap[index][z][0] != key:
                z += 1

            if z < len(self.hashMap[index]) and self.hashMap[index][z][0] == key:
                return self.hashMap[index][z][1]

            return -1

    def remove(self, key):

        if self.get(key) == -1: return

        # so we know it exists.
        index = key % 10000

        if len(self.hashMap[index]) == 1:
            self.hashMap[index] = []
            return

        z = 0

        while self.hashMap[index][z][0] != key:
            z += 1

        del self.hashMap[index][z]

if __name__ == '__main__':
    hm = MyHashMap()

    hm.put(10, 30)

    hm.get(10)
    hm.get(11)

    hm.put(10, 40)
    hm.put(11, 40)

    hm.remove(10)
