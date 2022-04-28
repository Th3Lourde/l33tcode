'''
[1,2,3]
[1,3,2]
[2,1,3]
     ^

Start right
go left until current element is greater then next element
if we hit idx 0, sort in ascending order


'''

class Solution:
    def nextPermutation(self, nums):
        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        # return idx
        def findPivot(arr):
            for j in range(len(arr)-2, -1, -1):
                if arr[j] < arr[j+1]:
                    return j

            return -1

        pivot_idx = findPivot(nums)

        if pivot_idx < 0:
            reverse(nums, 0, len(nums)-1)
            # print(nums)
            return

        # find the right most element that is greater than
        # the pivot
        successor_idx = 0

        for j in range(len(nums)-1, pivot_idx, -1):
            if nums[j] > nums[pivot_idx]:
                successor_idx = j
                break

        # Swap the two
        nums[pivot_idx], nums[successor_idx] = nums[successor_idx], nums[pivot_idx]

        # Reverse everything right of the pivot
        reverse(nums, pivot_idx+1, len(nums)-1)
        # print(nums)

Solution().nextPermutation([1,2,3])
Solution().nextPermutation([1,1,5])
Solution().nextPermutation([3,2,1])
