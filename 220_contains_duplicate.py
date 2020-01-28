'''
Given an array of integers, find out whether
there are two distinct indices i,j s.t.
|nums[i]-nums[j]| <= t
|i-j| <= k

We can't sort the array since that would 'destroy' the
sort of the indices. We can either have list sorted by
element value, indice value, or some bastard child of
the two. Not obvious the third would be helpful.

loop through each starting value, since we can make
predictions based upon i,j break the loop accordingly

We could always save the previous values that we have
seen to get rid of the second loop.

if t == 2, and nums[i] is fixed

|nums[i]-nums[j]| <= t             |nums[i]-nums[j]| <= t
nums[i] - nums[j] <= t             nums[i] - nums[j] >= -t
- nums[j] <= t - nums[i]           - nums[j] >= -t - nums[i]
nums[j] >= nums[i] + t             nums[j] <= t + nums[i]
'''


class Solution:

    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if len(nums) <= 1:
            return False

        vals = {}
        min = nums[0]
        max = nums[0]
        
        checked = {}

        for i in range(len(nums)):

            if nums[i] < min:
                min = nums[i]

            elif nums[i] >= max:
                max = nums[i]

            try:
                vals[nums[i]].append(i)

            except:
                vals[nums[i]] = [i]

        '''
        Have translated list to dict
        - Keys are sorted
        '''

        keys = list(vals.keys())
        keys.sort()


    # Also too slow
    def containsNearbyAlmostDuplicate_2(self, nums, k, t):
        for i in range(len(nums)-1):
            end = min(k+i+1, len(nums))

            for j in range(i+1, end):
                if abs(nums[i]-nums[j]) <= t and abs(i-j) <= k:
                    return True

        return False










    # didn't work
    def containsNearbyAlmostDuplicate_1(self, nums, k, t):

        if t < 0:
            return False

        # elif t == 0:
        #     for i in range(len(nums)):
        #         if abs(nums[i]-nums[i]) <= k:
        #             return True

        elif t > 0:
            for i in range(len(nums)-1):

                for j in range(i+1, len(nums)):

                    if (abs(nums[i]-nums[j]) <= t) and (abs(i-j) <= k):
                        return True

                    elif not(abs(i-j) <= k):
                        break

        return False




if __name__ == '__main__':
    s = Solution()

    nums = [1,2,3,1]
    k = 3
    t = 0

    print(s.containsNearbyAlmostDuplicate(nums,k,t))

    nums = [1,0,1,1]
    k = 1
    t = 2

    print(s.containsNearbyAlmostDuplicate(nums,k,t))

    nums = [1,5,9,1,5,9]
    k = 2
    t = 3

    print(s.containsNearbyAlmostDuplicate(nums,k,t))
