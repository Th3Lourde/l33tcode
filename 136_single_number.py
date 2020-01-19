
'''
Given a non-empty array of integers,
every element appears twice except for one.
Find that single one.
'''

class Solution:

    # brute-force: O(n) runtime, O(n+x?) memory complexity
    def singleNumber_brute(self, nums):
        d = {}

        for i in range(len(nums)):
            try:
                del d[nums[i]]

            except:
                d[nums[i]] = 1

        keys = list(d.keys())
        return keys[0]


    # [4,1,2,1,2]
    # [4,2,2]
    def singleNumber(self, nums):
        i = 0
        while True:

            if len(nums) == 1:
                break

            element = nums[i]

            if i == nums.index(element):
                i += 1

            elif i != nums.index(element):
                del nums[i]
                del nums[nums.index(element)]
                i -= 1


        return nums[0]


    def singleNumber_math(self, nums):
        # find all unique elements of nums
        # multiply all of the unique elements of nums by 2
        # subtracted by the sum of nums
        # runtime: O(n)
        # memory complexity: (space to create unique sum * 2) + (space to create sum(nums))
        # memory complexity: (number of unique elements)+(c)

        base = 0
        unique = set(nums)

        for i in range(len(nums)):
            base += nums[i]

        return sum(unique)*2 - base





if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))
