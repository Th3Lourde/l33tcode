class Solution:
    def maximumScore_1(self, nums, multipliers):
        dp = {}

        def itr(i,j,z,score):
            if z > len(multipliers)-1 or i > j:
                return score

            if (i,j,z) in dp:
                return dp[(i,j,z)]

            # calculate (i,j,ops)
            # either go left or right
            left = nums[i]*multipliers[z] + itr(i+1, j, z+1,0)
            right = nums[j]*multipliers[z] + itr(i, j-1, z+1,0)

            dp[(i,j,z)] = max(left,right)+score

            return dp[(i,j,z)]


        return itr(0,len(nums)-1,0,0)


    def maximumScore(self, nums, multipliers):
        n = len(nums)
        r = [0]

        for k, m in enumerate(multipliers, 1):
            rr = [-float('inf') for _ in range(k+1)]

            for i in range(k+1):
                j = k-i

                if i > 0:
                    rr[i] = max(rr[i], r[i-1] + m * nums[i-1])

                if j > 0:
                    rr[i] = max(rr[i], r[i] + m * nums[n-j])

            r = rr

        return max(r)



if __name__ == '__main__':
    s = Solution()
    print(s.maximumScore([1,2,3], [3,2,1]))
    print(s.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))

'''
Ok so understand this solution.
I thought that we needed to track i,j,z
We can actually infer what z is based upon i,j
so we can just track these two.

Ok so loop through the multipliers, start the counting at one.

Based upon the index of the multiplier, we have a few ways of
finding the max value possible.

If the multiplier has 4 multipliers before it, we need to consider
those other multipliers when finding the max value for this multiplier.

We have r, which is the max scores we had last round
And we have rr, which contains the max scores that we have this round

We both consider choosing from the left and from the right when we are
finding the max value for the multiplier.

We care about finding the max score on the ith operation.

The max score on the ith operation is reached either by picking from the
lhs or by picking from the rhs.

If we pick from the lhs,
then our answer is the max of the previous operation plus this operation.

Not sure why we have r[i] for the picking from right option

n = [-5,-3,-3,-2,7,1]
      ^
m = [-10,-5,3,4,6]
      ^
-------------------------------------------------
n = 6
r = [0]

k = 1
mult = -10

rr = [-10, 50]

Ok so yea my understanding was correct.

For each operation, we use what the previous max was in order to generate
the max to the current.

instead of doing mxm they just use two matrices

do it on paper, then code it up.




'''

# class Solution(object):
#     def maximumScore(self, nums, multipliers):
#         """
#         :type nums: List[int]
#         :type multipliers: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         r = [0]
#         for k, mult in enumerate(multipliers, 1):
#             rr = [-float('inf')] * (k+1)
#             for i in xrange(k+1):
#                 j = k-i
#                 if i > 0:
#                     rr[i] = max(rr[i], r[i-1] + mult * nums[i-1])
#                 if j > 0:
#                     rr[i] = max(rr[i], r[i] + mult * nums[n-j])
#             r = rr
#         return max(r)
