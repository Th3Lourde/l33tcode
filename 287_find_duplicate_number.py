

class Solution:
    def findDuplicate(self, nums):
        base = 0

        for i in range(1, len(nums)+1):
            base += i

        # print("base: {} actual: {}".format(base, sum(nums)))
        # print("len(nums)-diff = {}".format(len(nums)-abs(base-sum(nums))))

        return len(nums)-abs(base-sum(nums))




if __name__ == '__main__':
    s = Solution()
    # s.findDuplicate([1,3,4,2,2])
    s.findDuplicate([3,1,3,4,2])
