'''
Wow this was a fun problem.
dfs and binary search in one problem,
fun!


'''
import bisect as b

class Solution:
    def minAbsDifference(self, nums, goal):
        leftSums = set()
        rightSums = set()

        # Worked, but is too slow
        def findAllSums(arr, sumArr, idx, localSum, useSum):
            # if idx == 0:
            #     print("Arr: {}".format(arr))
            if useSum:
                sumArr.add(localSum)

            if idx >= len(arr):
                return

            for i in range(idx, len(arr)):
                # Skip current element
                findAllSums(arr, sumArr, idx+1, localSum, False)

                # Use current element
                findAllSums(arr, sumArr, idx+1, localSum+arr[idx], True)

        def dfs(i, cur, arr, sums):
            if i==len(arr):
                sums.add(cur)
                return
            dfs(i+1,cur,arr,sums)
            dfs(i+1,cur+arr[i],arr,sums)

        # findAllSums(nums[:len(nums)//2], leftSums, 0, 0, True)
        # findAllSums(nums[len(nums)//2:], rightSums, 0, 0, True)

        dfs(0, 0, nums[:len(nums)//2], leftSums)
        dfs(0, 0, nums[len(nums)//2:], rightSums)

        rightSums = list(rightSums)
        rightSums.sort()
        # rightSums=sorted(rightSums)

        # print(leftSums)
        # print(rightSums)

        # Find the closest value to targ
        # Too slow, but is correct
        def binarySearch(arr, targ):
            l = 0
            r = len(arr)-1

            diff = float('inf')
            idx = float('inf')

            while l < r:
                m = (l+r)//2
                currentDiff = abs(targ-arr[m])

                if currentDiff < diff:
                    diff = currentDiff
                    idx = m

                if arr[m] >= targ:
                    r = m

                else:
                    l = m+1

            # print("Initial: diff: {}, idx: {}".format(diff, idx))

            # While the element on the right is better, use it and continue
            # to look in that direction
            rM = m
            while rM < len(arr)-1 and abs(targ-arr[rM+1]) < diff:
                diff = abs(targ-arr[rM+1])
                idx = rM+1
                rM += 1

            # While the element on the left is better, use it and continue
            # to look in that direction
            lM = m
            while lM > 0 and abs(targ-arr[lM-1]) < diff:
                diff = abs(targ-arr[lM-1])
                idx = lM-1
                lM -= 1

            # print("Binary Search: (arr: {}, targ: {}) → {}".format(arr, targ, m))

            return arr[idx]

        ans = abs(goal)

        for e in leftSums:
            residual = goal-e

            # val = binarySearch(rightSums, residual)
            idx = b.bisect_left(rightSums, residual)

            if idx<len(rightSums):
                ans=min(ans,abs(residual-rightSums[idx]))
            if idx>0:
                ans=min(ans,abs(residual-rightSums[idx-1]))

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.minAbsDifference([5,-7,3,5], 6))
    print(s.minAbsDifference([7,-9,15,-2], -5))
    print(s.minAbsDifference([1,2,3], -7))
    print(s.minAbsDifference([-1,1,4,-4,9,-9,7,-7,3,2,3,5,6,4,8,9], 21))
