

class Solution:
    # def maxSumDivThree(self, nums: List[int]) -> int:

    '''
    This is if the nums[i]s must be consecutive
    '''

    def maxSumDivThree(self, nums):
        ans = 0

        nums.sort()

        d = {}

        for i in range(len(nums)):
            try:
                d[nums[i]] += 1
            except:
                d[nums[i]] = 1



        for i in range(len(nums)-1,-1,-1):

            if nums[i]%3 == 0:
                # if in dict add to ans
                if d[nums[i]] > 0:
                    d[nums[i]] -= 1
                    ans += nums[i]


            elif nums[i]%3 != 0:

                k = 0
                term = 3-nums[i]%3 + 3*k
                while term <= nums[i-1]:
                    j = 0

                    term = 3-nums[i]%3 + 3*k

                    while j < len(nums):
                        if nums[j] == term and d[term] > 0:
                            d[nums[j]] -= 1
                            d[nums[i]] -= 1
                            ans += nums[i] + nums[j]
                        break
                        j += 1

                    k += 1


        return ans


    def maxSumDivThree_1(self, nums):
        nums.sort()

        ans = 0

        for i in range(len(nums)):
            rang = nums[i:len(nums)]
            tmp = sum(rang)

            if tmp%3 == 0:
                if tmp > ans:
                    ans = tmp

            rang = nums[0:len(nums)-i]
            tmp = sum(rang)

            if tmp%3 == 0:
                if tmp > ans:
                    ans = tmp


            rang = nums[i]

            if rang%3 == 0:
                if rang > ans:
                    ans = rang


        return ans

        '''
        if sum %3 == 0, is divisible by three
        '''

if __name__ == '__main__':
    s = Solution()

    nums = [3,6,5,1,8]

    print(s.maxSumDivThree(nums))
