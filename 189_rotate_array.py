
'''
Given an array, rotate the array to the right
k steps, where k is non-negative

copy nums[k-1]

[1,2,3,4,5,6,7]
k = 3

replace in a cyclic-like fashion
the number of cycles is represented
by k
'''


class Solution:

    def rotate(self, nums, k):

        if len(nums) > 1 and k > 0:
            if k > len(nums):
                k -= k//(len(nums))*(len(nums))

            cpy = nums[len(nums)-k:]
            print(cpy)

            i = len(nums)-1

            while i > k-1:
                nums[i] = nums[i-k]
                i -= 1

            nums[:k] = cpy

        print(nums)

    # brute-force, not fast enough
    def rotate_1(self, nums, k):
        for j in range(k):
            tmp =  nums[0]
            for i in range(len(nums)-1):
                tmp2 = nums[i+1]
                nums[i+1] = tmp
                tmp = tmp2

            nums[0] = tmp





if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    s.rotate(nums, k)
