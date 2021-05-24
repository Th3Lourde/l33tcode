'''
Ok so I was correct in two pointers, I just didn't come
up with a fast enough solution.

So we have i,j. We want to avoid increasing the min at all
costs.

Every iteration, we decide if we want to increase i, j.

If i > min, do it
If not i but j > min do it
If both i and j are < min, pick the larger of the two

Honestly I think you can just simplify this to picking the larger
of the two.




'''

class Solution:
    # Correct, too slow
    def maximumScore_1(self, nums, k):
        maxScore = 0

        minStack = [0 for _ in range(len(nums))]
        minVal = nums[k]

        for i in range(k, len(nums)):
            if nums[i] < minVal:
                minVal = nums[i]

            minStack[i] = minVal

        leftMin = nums[k]

        for l in range(k, -1, -1):
            if nums[l] < leftMin:
                leftMin = nums[l]

            for r in range(k, len(nums)):
                tmpScore = min(leftMin, minStack[r])*(r-l+1)

                if tmpScore > maxScore:
                    maxScore = tmpScore

        return maxScore

    def maximumScore(self, nums, k):
        score = nums[k]
        minE = nums[k]

        i = k
        j = k

        while i > 0 or j < len(nums)-1:
            if i-1 >= 0 and j+1 <= len(nums)-1:
                if nums[i-1] >= nums[j+1]:
                    i -= 1
                else:
                    j += 1

            elif i-1 >= 0:
                i -= 1

            else:
                j += 1

            minE = min(minE, nums[i], nums[j])

            score = max(score, minE*(j-i+1))

        return score




s = Solution()

print(s.maximumScore([1,4,3,7,4,5], 3))
print(s.maximumScore([5,5,4,5,4,1,1,1], 0))
