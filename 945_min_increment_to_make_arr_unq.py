class Solution:
    def minIncrementForUnique(self, arr):
        if not arr:
            return 0

        arr.sort()

        ops = 0
        prevMax = arr[0]

        for i in range(1, len(arr)):
            if arr[i] <= prevMax:
                ops += prevMax-arr[i]+1

            prevMax = max(arr[i], prevMax+1)

        return ops

s = Solution()

print(s.minIncrementForUnique([1,2,2]))
print(s.minIncrementForUnique([3,2,1,2,1,7]))
