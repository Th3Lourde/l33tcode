'''
Ok let's give this a good honest effort
for an hour, then move on.

We are given, two integers:
n, maxValue

We care about describing ideal arrays.

An array is an ideal array iff:
- every element in the array is in [0, maxValue]
- for every element arr[i] is divisible by arr[i-1] (0,n)

Given n, maxValue, return the number of distinct ideal arrays
of length n

So I have a brute-force backtracking algo, perhaps we can
use a set in order to not double count.

When going to the next iteration of backtracking, we
can either use the number we were using before, or
a number that is divisible by the previous number.

Yea I'm not really sure how to make the backtracking algo
occur without touching combinations where a double-count
occurs.

We can just store the arrays as a set of tuples, then
transform them back.

Run-time: something factorial. Some math expression.
memory complexity: also something factorial

I count TLE on LC hards as a victory.
'''

class Solution:
    def idealArrays(self, n, maxValue):
        ans = set()

        choiceList = [i for i in range(1, maxValue+1)]

        def backtrack(arr, opts):
            if len(arr) == n:
                ans.add(tuple(arr))
                return

            for idx in range(len(opts)):
                if len(arr) > 0:
                    if (opts[idx] % arr[-1] == 0):
                        # print("{} % {} == {}".format(arr[-1], opts[idx], arr[-1] % opts[idx] == 0))
                        arr.append(opts[idx])
                        backtrack(arr, opts[idx:])
                        arr.pop()
                else:
                    arr.append(opts[idx])
                    backtrack(arr, opts[idx:])
                    arr.pop()

        backtrack([], choiceList)

        # print(ans)

        return len(ans)

print(Solution().idealArrays(5, 3)) # 11
print(Solution().idealArrays(2, 5)) # 10
