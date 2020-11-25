
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r) // 2

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if nums[l] != target:
            return -1

        return l


if __name__ == '__main__':
    s = Solution()
