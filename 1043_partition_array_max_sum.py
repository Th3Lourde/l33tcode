'''
Populate dp for the first k-1, then just
refer to the dp for future calls

[1,15,7,9,2,5,10] | k = 3
      i

dp = [1,30,45,-1,-1,-1,-1]

itr(dp, 0)

maxPartition = 1
maxVal = 1
'''
class Solution:
    # Bottom Up
    def maxSumAfterPartitioning(self, arr, k):
        dp = [float('-inf') for _ in range(len(arr))]

        maxVal = float('-inf')

        for i in range(k):
            if arr[i] > maxVal:
                maxVal = arr[i]

            dp[i] = maxVal*(i+1)

        for i in range(k, max(k, len(arr))):
            maxVal = float('-inf')

            for z in range(i, i-k, -1):
                # print(z)
                if arr[z] > maxVal:
                    maxVal = arr[z]

                partition = dp[z-1]+maxVal*(i-z+1)

                if partition > dp[i]:
                    dp[i] = partition

        # print(dp)
        return max(dp[len(dp)-k:])

    # Top Down
    def maxSumAfterPartitioning_1(self, arr, k):
        dp = [-1 for _ in range(len(arr))]

        def itr(dp, i):
            if i >= len(arr):
                return 0

            if dp[i] != -1:
                return dp[i]

            maxPartition = arr[i]
            maxVal = arr[i]

            for z in range(i, min(i+k,len(arr))):
                maxVal = max(maxVal, arr[z])
                maxPartition = max(maxPartition, maxVal*(z-i+1)+itr(dp, z+1))

            dp[i] = maxPartition

            return dp[i]

        itr(dp, 0)

        return max(dp[0:k+1])

s = Solution()

print(s.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)) # 84
print(s.maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4)) # 83
print(s.maxSumAfterPartitioning([1], 1)) # 1
