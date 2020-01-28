'''
List is read only
Can only use constant space
0(n) < 0(n^2)
There is only one element in the array
that has a frequency > 1, however that
frequency can be <= n

Write an algorithm that can identify
said element
'''

class Solution:

    def findDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)



    # kinda bullshit, only one answer meets
    # the requirements. Other solutions do
    # not abide by constraints
    def findDuplicate_2(self, nums):
        actual = sum(nums)

        unique = 0

        for i in range(len(nums)):
            if i in nums:
                actual -= i
                unique += 1

        return int(actual/(len(nums)-unique))


    # did not work
    def findDuplicate_1(self, nums):
        base = 0

        for i in range(1, len(nums)+1):
            base += i

        # print("base: {} actual: {}".format(base, sum(nums)))
        # print("len(nums)-diff = {}".format(len(nums)-abs(base-sum(nums))))

        return len(nums)-abs(base-sum(nums))




if __name__ == '__main__':
    s = Solution()
    # s.findDuplicate([1,3,4,2,2])
    print(s.findDuplicate([1,3,4,2,2]))
