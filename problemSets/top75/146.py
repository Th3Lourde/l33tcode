from pqdict import PQDict

class LRUCache:

    def __init__(self, capacity):
        self.ops = 0
        self.c = capacity
        self.dict = {}
        self.heap = PQDict()

    def get(self, key):
        if key not in self.dict:
            return -1

        self.ops += 1

        self.heap.updateitem(key, self.ops)
        return self.dict[key]


    def put(self, key, value):
        self.ops += 1

        if key in self.dict:
            self.heap.updateitem(key, self.ops)

        else:
            self.dict[key] = value
            self.heap.additem(key, self.ops)

        if len(self.heap) > self.c:
            itemToDel, _ = self.heap.popitem()
            del self.dict[itemToDel]





lru = LRUCache(3)

lru.put(1,1)
lru.put(2,2)
lru.put(3,3)

lru.get(3)
lru.heap

lru.put(5,5)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
