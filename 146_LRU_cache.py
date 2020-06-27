'''
So we have something called a
Least Recently Used cache

While our other stacks didn't allow
us to add new elements, this does.

This is a cache that we can keep
adding to no matter what. We don't
care about size. What we should
care about is which element we have
used most recently.

We have this cache, initialized
to [None]*capacity

left most side represents the most
recently used element.

when we add and element:

put at lhs of cache.
If len cache is over capacity, pop.
If we initialize [None]*capacity,
wouldn't we always be over capacity?
I think so. Let's test it.

We should also have a quick lookup.
What we could do, is store a separate
dict with the key val pairs

When we remove an element, we set the key
to None

If the key already exists,
get the key.
'''

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = [None]*capacity
        self.dict = {}

    def __repr__(self):
        return " dict: {}\ncache: {}".format(self.dict, self.cache)

    def get(self, key):
        # search for the key
        # remove it from where
        # it is and put it at
        # the front.

        i = 0
        ret = 0

        while i < self.capacity and self.cache[i] != key:
            i += 1

        if i < self.capacity and self.cache[i] == key:
            del self.cache[i]
            self.cache = [key] + self.cache
            ret = 1

        if ret:
            return self.dict[key]

        return -1

    def put(self, key, value):
        # check if the key already
        # exists

        try:
            if self.dict[key] != None:

                # give it the correct value
                self.dict[key] = value
                return self.get(key)

            elif self.dict[key] == None:
                # The value is not in our cache
                self.dict[key] = value

                self.cache = [key] + self.cache

                r = self.cache.pop()

                if r != None:
                    self.dict[r] = None

        except:
            # if the key doesn't exist,
            # add it to dict
            self.dict[key] = value

            # update our cache

            self.cache = [key] + self.cache

            r = self.cache.pop()

            if r != None:
                self.dict[r] = None


if __name__ == '__main__':
    cache = LRUCache(3)

    cache

    cache.put(1,1)
    cache.put(2,2)
    cache.put(3,3)
    cache.put(4,4)

    cache.get(1)
    cache.get(2)

    cache.get(3)
    cache.get(4)

    cache
