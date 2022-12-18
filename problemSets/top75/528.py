import random
import bisect

class Solution:
    def __init__(self, w):
        self.arr = []
        self.prefixWeightToIdx = {}
        sum = 0

        for idx, weight in enumerate(w):
            sum += weight
            self.arr.append(sum)
            self.prefixWeightToIdx[sum] = idx


    def pickIndex(self):
        idx = random.randint(1, self.arr[-1])
        insert_point = bisect.bisect_left(self.arr, idx)
        weightSelected = self.arr[insert_point]

        return self.prefixWeightToIdx[weightSelected]

wd = Solution([1,3,4,5])

print(wd.arr)


for _ in range(14):
    print(wd.pickIndex())
