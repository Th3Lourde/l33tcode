'''
Max score performing multiplications
operations

Given two integer arrays nums, multipliers
len(nums) == n
len(multipliers) == m

n >= m

arrays are 1-indexed

Score is initially zero

perform m operations

on the ith operation:
choose one integer x, x is at the start or end of nums
score += multipliers[x]
remove x from score

get max score

basically, you can chose left, right, left,
get max score.

recursion?

yea, but will probably TLE

you are two choices: l, r

dp could be (i,j), to represent the options that are available

dp = (i,j,ops)

if multipliers is positive and left or right is positive:
    choose the biggest one.

if multipliers is positive and left and right is negative:
    choose the biggest one

if multipliers is negative, choose the smallest one

5

[-5,-3,-3,-2,7,1]

'''

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
        l = 0
        r = len(nums-1)





    def maximumScore_2(self, nums, multipliers):
        l = 0
        r = len(nums)-1
        ans = 0

        for m in multipliers:
            if m == 0:
                # DP?
                ...

            elif m > 0:
                # Chose the largest option
                if nums[l] > nums[r]:
                    ans += nums[l]*m
                    l +=1
                else:
                    ans += nums[r]*m
                    r -=1
            else:
                if nums[l] < nums[r]:
                    ans += nums[l]*m
                    l +=1
                else:
                    ans += nums[r]*m
                    r -=1

        return ans





if __name__ == '__main__':
    s = Solution()
    print(s.maximumScore([1,2,3], [3,2,1]))
    print(s.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
