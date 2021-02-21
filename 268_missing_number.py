
class Solution:
    def missingNumber(self, nums):
        s = set()

        for i in range(len(nums)+1):
            s.add(i)

        for n in nums:
            s.remove(n)

        return s.pop()

if __name__ == '__main__':
    s = Solution()

    print(s.missingNumber([3,0,1]))
