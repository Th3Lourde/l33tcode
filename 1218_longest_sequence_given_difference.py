'''
Given integer array arr
and integer difference

Find a sequence of adjacent elements such
that the difference between every element
is difference

We can remove as many elements as we want.
Get the longest chain that's possible.

We def shouldn't take both. One later in day is best.

Start with rhs and move forwards, keep set of element
with value being the length of the sequece

looking for number + difference

[1,5,7,8,5,3,4,2,1] | -2
       ^

targ = 8 + -2 = 6

{
 1:1,
 2:1,
 4:2,
 3:2,
 5:3,
 8:1,
 7:4,
 5:3,


}

Ok so I'm pretty sure that I just cracked it.

'''

class Solution:
    def longestSubsequence(self, arr, difference):
        dp = {}
        maxRun = 1

        for i in range(len(arr)-1, -1, -1):
            run = 1
            e = arr[i]

            if e + difference in dp:
                run += dp[arr[i]+difference]

            if e not in dp:
                dp[e] = run
            elif run > dp[e]:
                dp[e] = run

            if run > maxRun:
                maxRun = run

        # print(dp)

        return maxRun

s = Solution()

print(s.longestSubsequence([1,5,7,8,5,3,4,2,1], -2))
print(s.longestSubsequence([1,3,5,7], 1))
print(s.longestSubsequence([1,2,3,4], 1))
