

class Solution:
    def rob(self, nums):
        '''
        Ok so you can't rob adjacent houses.
        My initial thought is that you just sum
        the values of the evenly numbered houses
        and compare that to the sum of the oddly
        numbered houses, and return the max value
        '''
        odd = 0
        even = 0

        bool = True

        for i in range(len(nums)):
            if bool:
                even += nums[i]
                bool = False
            elif not bool:
                odd += nums[i]
                bool = True

        return max(odd, even)

if __name__ == '__main__':
    s = Solution()

    # houses = [1,2,3,1]
    houses = [2,7,9,3,1]


    print(s.rob(houses))
