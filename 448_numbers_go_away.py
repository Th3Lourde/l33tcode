

class Solution:
    # These are both correct
    def findDisappearedNumbers(self, nums):
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)

        return ans

    def findDisappearedNumbers_1(self, nums):
        obs = set()
        exp = set()

        for i in range(len(nums)):
            obs.add(nums[i])
            exp.add(i+1)

        return exp-obs


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
