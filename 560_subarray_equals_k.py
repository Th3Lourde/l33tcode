

'''
Sub aray can contain both positive and negative
numbers, so we can't stop if we are above target

0(n^2) solution: Just create all possible continuous
subarrays and record when we are at target.

[1,1,1]
     ^

[3, 2, 1]

1) Go through all elements and add current element, check if k
2) Check if current element is k, append the current element
-- If k += 1 to ans

Still 0(n²) but a bit cleaner

[1,1,1] | 2
     ^

[3,2,1]
2

[1,2,3], 3
     ^

[3,2]
1

Correct but too slow, as I thought

Also predicted that this was a prefix sum problem,
which it is, I didn't know prefix sums. I just 'learned' them

            # look for number of times
            # run has had a value of n-k
            # b/c v = n-k ^ v+k=n are instances that we care about
'''

class Solution:
    # O(n²)
    def subarraySum_1(self, nums, k):
        subArrays = []
        ans = 0

        for n in nums:
            for idx in range(len(subArrays)):
                subArrays[idx] += n

                if subArrays[idx] == k: ans += 1

            if n == k:
                ans += 1

            subArrays.append(n)

        return ans

    # 0(n)
    def subarraySum_2(self, nums, k):
        historic_sum = {0:1}
        ans = 0
        run = 0

        for n in nums:
            run += n
            ans += historic_sum.get(run-k, 0)
            historic_sum[run] = historic_sum.get(run, 0) + 1

        return ans

    def subArraySum(self, nums, k):
        arrSum = 0
        currentSum = 0
        d = {0:1}

        for idx, val in enumerate(nums):
            currentSum += val

            if currentSum-k in d:
                arrSum += d[currentSum-k]

            if currentSum in d:
                d[currentSum] += 1
            else:
                d[currentSum] = 1

        return arrSum

'''
Update sum

d[sum] = counter

arrSum = 0
sum = 2

1 1 1 | k = 2
  ^

d = {
    1:1
    2:1
    3:1
}

'''




s = Solution()
print(s.subArraySum([1,1,1], 2))
print(s.subArraySum([1,2,3], 3))
print(s.subArraySum([], 3))
