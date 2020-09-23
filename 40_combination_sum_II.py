
'''
Given a collection of candidate
numbers and a target number,
find all unique combinations
in candidates where the candidate
numbers sum to targ.

All numbers will be positive.

1) Sort the numbers
2) get rid of any numbers that are bigger
  than our target.
3) Use backtracking algorithm

e.g. :

[10,1,2,7,6,1,5]

1 1 2 5 6 7 10 | 8

1 1 2 5 6 7

1
11
12
15
16
17

112
115
116
117
125
126
127
...

Also make this recursive

nums = List[int]

(idx, vals, sum)

if sum == targ:
    ans.append(vals)
    return

for i in range(idx, len(nums)):
    func(i+1, vals + [nums[i]], sum+nums[i])


Could done the test cases better.

That's just kinda how it goes though.

I did a good job recognizing the pattern and then executing
it.

Tbh that is pretty much as good as you can expect. Got it
in 30mins, keep going.

This keyboard doesn't have a backlight. That's ok, I usually
go by touch anyways.

Ok, next question


'''

class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()

        while len(candidates) > 1 and candidates[-1] > target:
            candidates.pop()

        ans = []
        seen = set()

        def itr(idx, vals, sum):
            if sum == target:
                if tuple(vals) not in seen:
                    ans.append(vals)
                    seen.add(tuple(vals))
                return

            for i in range(idx, len(candidates)):
                if candidates[i] + sum <= target:
                    itr(i+1, vals+[candidates[i]], sum+candidates[i])


        itr(0, [], 0)

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.combinationSum2([10,1,2,7,6,1,5], 8))

    print(s.combinationSum2([2,5,2,1,2], 5))

    print(s.combinationSum2([2,5,2,1,2], 7))

    print(s.combinationSum2([2], 1))
