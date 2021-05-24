'''
So the question is: can we make a subset
that sums to sum(nums)//2 ?

Maybe dp could be can we make a subset that
sums to x?

We could then store the indices used to make the sum.
If there is any overlap then we know not to use it.

I can think of a bottom-up solution where we have
rows be the elements in our solution set and the columns
be the value of our sum.
However if we do this with an array it could result in
worse time complexity due to the size of the dp.

I've tried three solutions. Let's write down our thoughts
and then look.

1) dp[targ], where we see if we can create a sum equal to target.
Record the elements that we use in order to create the sum. See
if you can create a mapping that works.

2) bottom-up dp: 0,1,2,...,targ, ever time we add a new number to
the solution set, see what sums we can come up with.

Problem is the size of the solution set. Although this is better than
exponential time. Idk, let's shave then try it. Good practice.

[1,5,11,5]

22//2 = 11

n|0,1,2,3,4,5,6,7,8,9,10,11
1|T,T,F,F,F,F,F,F,F,F,F ,F
5|T,T,F,F,F,T,T,F,F,F,F ,F
5|T,T,F,F,F,T,T,F,F,F,F ,T

initially, just set the value to true

dp[i][val] = dp[i][val-nums[i]] or dp[i-1][val]

Ok so just use one list then

[2,2,1,1] sum ==6, goal 3
     ^

n|0,1,2,3
-|T,F,F,F
2|T,F,T,F
2|T,T,T,T

[1,2,5] || sum == 8, targ 4
 ^

n|0,1,2,3,4
-|T,F,F,F,F
1|T,T,

'''
class Solution:
    # Correct, too slow
    def canPartition_1(self, nums):
        def itr(idx, s1, s2):
            if idx >= len(nums):
                return True if s1 == s2 else False

            return itr(idx+1, s1+nums[idx], s2) or itr(idx+1, s1, s2+nums[idx])

        return itr(0, 0, 0)

    # Also correct, also too slow
    def canPartition_2(self, nums):
        s = sum(nums)

        if s%2 == 1:
            return False

        targ = s//2

        def itr(idx, mySum):
            if idx >= len(nums) or mySum < 0:
                return False
            elif mySum == 0:
                return True

            for i in range(idx, len(nums)):
                if nums[i] > mySum:
                    continue

                if itr(i+1, mySum-nums[i]) == True:
                    return True

            return False

        return itr(0, targ)

    # Also correct, got it!
    def canPartition_3(self, nums):
        s = sum(nums)

        if s%2 == 1:
            return False

        targ = s//2

        dp = [False for _ in range(targ+1)]
        dp[0] = True

        for i in range(len(nums)):
            if nums[i] > targ:
                continue

            dp2 = list(dp)

            for t in range(0, targ+1):

                if dp[t] == True and t+nums[i] <= targ:
                    dp2[t+nums[i]] = True

            dp = dp2

        return dp[targ]

    # Ok so let's now try a set
    # Set isn't that much better
    def canPartition(self, nums):
        s = sum(nums)

        if s%2 == 1:
            return False

        targ = s//2

        dp = set({0})

        for i in range(len(nums)):
            if nums[i] > targ:
                continue

            dp2 = set(dp)

            for t in range(0, targ+1):
                if t in dp and t+nums[i] <= targ:
                    dp2.add(t+nums[i])

            dp = dp2

        return targ in dp





if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1,5,11,5])) # True
    print(s.canPartition([1,2,3,5])) # False
    print(s.canPartition([1,2,5])) # False
    print(s.canPartition([2,2,1,1])) # True
