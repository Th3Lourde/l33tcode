'''
Oh no, so we are told where to insert the value.
So keep a pointer located initially at the lhs of
the queue. So insert value, while stream[ptr] != None,
append(stream[ptr]) and += 1 to ptr.

'''

class Solution:
    def __init__(self, n):
        self.stream = [None for _ in range(n+1)]
        self.ptr = 1
        self.n = n

    def insert(self, idKey, value):
        self.stream[idKey] = value

        resp = []

        while self.ptr < self.n+1 and self.stream[self.ptr] != None:
            resp.append(self.stream[self.ptr])
            self.ptr += 1

        return resp
