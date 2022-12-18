'''
1. Find the largest index i such that array[i-1] < array[i] (if dne, this is the largest permutation)
2. Find the largest index j such that j >= i and array[j] > array[i-1]
3. Swap array[j] and array[i-1]
4. Reverse the suffix starting at array[i]
'''

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        # 1. Find the largest index i such that array[i-1] < array[i]
        # if dne, this is the largest permutation
        idx = -1

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                idx = i

        if idx == -1:
            # return reversed
            # nums = nums[::-1]
            nums = nums.reverse()
            return nums

        # 2. Find the largest index j s.t. j >= i and array[j] > array[i-1]
        j = i
        for tmpJ in range(idx, n):
            if nums[tmpJ] > nums[idx-1]:
                j = tmpJ

        # 3 swap array[j] and array[i-1]
        nums[j], nums[idx-1] = nums[idx-1], nums[j]

        # 4 reverse the suffix starting at array[i]
        suffix = nums[idx:]
        suffix = suffix[::-1]
        nums[idx:] = suffix
        return nums

print(Solution().nextPermutation([1,3,2]))
print(Solution().nextPermutation([3,2,1]))
print(Solution().nextPermutation([1,1,5]))

a = [1,2,3,3,2,1]
suffix = a[3:]
suffix = suffix[::-1]
a[3:] = suffix
a
