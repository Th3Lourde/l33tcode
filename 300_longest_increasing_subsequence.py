class Solution:
    # 0(n²)
    def lengthOfLIS_2(self, arr):
        dp = [0 for _ in range(len(arr))]
        dp[0] = 1

        for i in range(1, len(arr)):
            longestSubSequence = 0
            for j in range(i-1, -1, -1):
                if arr[j] < arr[i] and dp[j] > longestSubSequence:
                    longestSubSequence = dp[j]
            dp[i] = longestSubSequence+1

        return max(dp)

    # Too slow
    def lengthOfLIS_1(self, arr):
        dp = [[] for _ in range(len(arr))]

        def helper(idx, sequence):
            if idx >= len(arr):
                return sequence

            if dp[idx]:
                return dp[idx]

            ans = [arr[idx]]

            for i in range(idx+1, len(arr)):
                if arr[i] > arr[idx]:
                    resp = sequence + helper(i, [arr[i]])

                    if len(resp) > len(ans):
                        ans = resp

            dp[idx] = ans
            return dp[idx]

        ans = []

        for i in range(len(arr)):
            r = helper(i, [arr[i]])
            if len(r) > len(ans):
                ans = r

        return len(ans)

    def lengthOfLIS(self, arr):
        dp = []

        def binarysearch(arr, targ):
            l = 0
            r = len(arr)-1

            closest = r

            while l < r:
                m = l + (r-l)//2

                if arr[m] == targ:
                    closest = m
                    break
                elif arr[m] < targ:
                    l = m+1
                else:
                    if abs(targ-arr[m]) < abs(targ-arr[closest]):
                        closest = m
                    r = m

            return closest

        for e in arr:
            if not dp:
                dp.append(e)
            elif e > dp[-1]:
                dp.append(e)
            else:
                # Find the smallest # > e, replace it.
                idx = binarysearch(dp, e)

                dp[idx] = e

        return len(dp)


s = Solution()

print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6])) # 6


print(binarysearch([1,3,5,7,9], 9))

'''
If dp is empty, add element

If dp isn't, binary search for element.

We want to form the smallest possible sequence.

If our current element is larger than largest element,
append it to the sequence.

If our current element is not larger than largest element,
Find the
'''
