class Solution:
    def isPossibleDivide(self, nums, k):
        d = {}

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        # print(d)

        keys = list(d.keys())
        keys.sort()

        for z in keys:
            while d[z] != 0:
                # print("dict1: {}".format(d))
                if d[z] == 0:
                    continue

                for i in range(z, k+z):
                    # print("i: {} | dict2: {}".format(i, d))
                    if i in d and d[i] > 0:
                        d[i] -= 1
                    else:
                        return False

        return True

s = Solution()

print(s.isPossibleDivide([3,3,2,2,1,1], 3)) # True
print(s.isPossibleDivide([3,3,3,2,2,2,1,1,1], 3)) # False
print(s.isPossibleDivide([3,3,3,2,2,2,1,1], 3)) # False

print(s.isPossibleDivide([1,2,3,3,4,4,5,6], 4)) # True
print(s.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3)) # True
print(s.isPossibleDivide([1,2,3,4], 3)) # False
