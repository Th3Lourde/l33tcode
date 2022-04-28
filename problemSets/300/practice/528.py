import random

class Solution:
    def __init__(self, w):
        self.arr = w
        self.n = len(w)

        for i in range(1, self.n):
            self.arr[i] += self.arr[i-1]

        self.s = self.arr[-1]

    def pickIndex(self):
        rand_num = random.randint(1, self.s)

        l = 0
        r = len(self.arr)-1

        while l < r:
            m = (l+r)//2

            if rand_num <= self.arr[m]:
                r = m
            else:
                l = m+1

        return l

w = Solution([1,3,7,2,1,5])
w = Solution2([1,3,7,2,1,5])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
