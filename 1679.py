'''
Max Numbers of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers form the array whose sum equals k
and remove them from the array.

Return the maximum number of operations you can perform on the array.

So this problem is pretty straight forwards. One thing that is helpful
is that it doesn't matter in which order you remove the pairs, and it
is very simple to decide which pair to remove.

Create a dict,
loop through dict,
if a pair exists (k-key1), decrement key1 and d[k-key1], increment ans
else delete the key.
continue until dict is empty

key1+key2 = k
key2 = k-key1

0(n) time complexity
0(n) space complexity

2

target=2-1=1

{1: 4, 3: 3, 2: 4, 5: 4}
 ^
'''

class Solution:
    def maxOperations_1(self, nums, k):
        numToFreq = {}
        ans = 0

        for num in nums:
            if num in numToFreq:
                numToFreq[num] += 1
            else:
                numToFreq[num] = 1

        # print(numToFreq)
        # return

        while len(numToFreq) > 0:
            for key in numToFreq:
                target = k-key

                if target not in numToFreq:
                    del numToFreq[key]

                elif target == key:
                    if numToFreq[target] == 1:
                        del numToFreq[key]
                    else:
                        ans += numToFreq[target] // 2
                        numToFreq[target] -= 2*(numToFreq[target] // 2)

                        if numToFreq[key] == 0:
                            del numToFreq[key]

                else:
                    minVal = min(numToFreq[key], numToFreq[target])
                    ans += minVal

                    numToFreq[key] -= minVal
                    numToFreq[target] -= minVal

                    if numToFreq[key] == 0:
                        del numToFreq[key]

                    if numToFreq[target] == 0:
                        del numToFreq[target]

                break


        return ans

    def maxOperations(self, nums, k):
        numToFreq = {}
        ans = 0

        for num in nums:
            target = k-num

            if target in numToFreq:
                ans += 1

                if numToFreq[target] == 1:
                    del numToFreq[target]
                else:
                    numToFreq[target] -= 1
            else:
                if num in numToFreq:
                    numToFreq[num] += 1
                else:
                    numToFreq[num] = 1

        return ans





print(Solution().maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))
print(Solution().maxOperations([3,3,1,3,4,3], 6))
print(Solution().maxOperations([], 5))
print(Solution().maxOperations([3,1,3,4,3], 2))
print(Solution().maxOperations([3,1,3,4,3], 6))
print(Solution().maxOperations([1,2,3,4], 5))
