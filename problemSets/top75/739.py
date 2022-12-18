'''
Given an integer array that represents
the daily temperatures,

return an array such that array[i] is
the number of days you have to wait after
the ith day to get a warmer temp.

If there is no such day, let it be zero.

I'm going to guess stack. Not sure why.
Monotonically increasing stack?

        2           6

          2  1  1   0  0
[73,74,75,71,69,72,76,73]
          ^
[71,72,76]
d=2

Ok start

'''

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0]*len(temperatures)
        idx = len(temperatures)-1

        while idx >= 0:
            # solve for arr[i]
            while stack:
                if stack[-1][0] > temperatures[idx]:
                    ans[idx] = stack[-1][1]-idx
                    break
                else:
                    stack.pop()

            # add element to stack
            stack.append((temperatures[idx], idx))

            idx -= 1

        return ans

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
