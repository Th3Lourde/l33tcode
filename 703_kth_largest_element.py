class KthLargest: # Works, is very slow.

    def __init__(self, k: int, nums: List[int]):
        self.heap = list(nums)
        self.heap.sort(reverse = True)
        self.heap = self.heap[:k]
        self.k = k

    def add(self, val: int) -> int:
        z = len(self.heap) - 1
        insertAt = None

        if len(self.heap) < self.k:
            if len(self.heap) == 0:
                self.heap.append(val)
                return val

            insertAt = z+1

        while val > self.heap[z] and z >= 0:
            insertAt = z
            z -= 1

            if z < 0:
                insertAt = 0
                break

        if type(insertAt) == type(1):
            self.heap.insert(insertAt, val)

            if len(self.heap) > self.k:
                self.heap.pop()

        return self.heap[self.k-1]
