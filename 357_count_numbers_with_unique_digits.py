'''
Just do as the problem says, count all numbers with unique digits.

Input: 2

0 ≤ x < 10ⁿ ⟹ 0 ≤ x < 10² ⟹ 0 ≤ x < 10²

Count all digits of length 1: [0,1,2,3,4,5,6,7,8,9]
Count all digits of length 2: [12,13,14,...]
    So for i in range(1, 10):
        i*8 (Count the first digit, no repeats)

Count all digits of length 3: [123,124,125]
    for i in range(1, 10):
        i*7 ← Wouldn't this just be the answer for 2, then each term has 7 options?

Go until you get up to terms of length n-1. (for this case less than 100)

So how could we do some DP for this?

Given a term of length y (with unique digits), how many terms can you generate with
length y+1? (with unique digits?)

For a single term of length y, can generate 9-y new terms

So if we have x terms of length y, generate z = x*(9-y) new terms

Then if we have z terms of length y+1, generate w = z*(9-y+1) new terms

...

(Omit zero for now, add on at end)

itr(terms, current, goal):
    # "Base case"/Setup, n=1

    if current >= goal:
        return terms+1

    elif current == 1:
        itr(9, current+1, goal)

        # current > 1
    else:

        if 9-current < 1:
            return terms+1

        additions =

        itr(terms+terms*(9-current), current+1, goal)

n = 3

(terms, current, goal)

(0, 1, 3)

(9, 2, 3)

# 9-2 == 7 > 5 ⟹ itr(9+9*(5))

(terms, in_running, current, goal)

n = 1

# current --> length of in_running
(1, 9, 1, 3)

tmp = 0

for i in range(in_running):
    tmp += 9-current


itr(1, 9, 1, 3)

9-in_running == 8 && 1+1 == 2

tmp = 0
[0,1,2,3,4,5,6,7,8,9]
[12,13,14,15,16,17,18,19]
[21,23,24,25,26,27,28,29]
[31,23,24,25,26,27,28,29]
[41,23,24,25,26,27,28,29]
[51,23,24,25,26,27,28,29]
[51,23,24,25,26,27,28,29]
[51,23,24,25,26,27,28,29]
[51,23,24,25,26,27,28,29]
[51,23,24,25,26,27,28,29]

for i in range(in_running (9)):
    tmp += 10-current (9)

(tmp == 81)

(10, 81, 2, 3)

'''

class Solution:

    def countNumbersWithUniqueDigits(self, n):

        if n == 0: return 1
        elif n == 1: return 10

        def itr(terms, in_running, current):
            # Maybe change goal to be == 9
            # if in_running == 0 or 10-current < 1 or current == n:
            if in_running == 0 or current == n:
                return terms+in_running

            else:
                tmp = 0

                for i in range(in_running):
                    tmp += 10-current

                return itr(terms+in_running, tmp, current+1)

        return itr(1, 9, 1)


    def countNumbersWithUniqueDigits_1(self, n):

        ans = [0]

        if n == 0: return 1

        def itr(nums, opts, maxLen, ans):

            if len(nums) == maxLen:

                if nums[0] == 0: return

                if len(nums) == n+1 and nums[0] < 1:
                    # print(nums)
                    ans[0] += 1
                    return

                elif len(nums) == n+1 and nums[0] == 1 and nums[1:] == [0 for i in range(n+1)] :
                    # print(nums)
                    ans[0] += 1
                    return

                elif len(nums) != n+1:
                    # print(nums)
                    ans[0] += 1
                    return

            for i in range(len(opts)):
                if opts[i] not in nums:
                    # nums.add(i)
                    # nums.append(i)
                    itr(nums + [opts[i]], opts[:i]+opts[i+1:], maxLen, ans)
                    # nums.remove(i)
                    # nums.pop()

        opts = [i for i in range(1,10)] + [0]

        for maxLen in range(1, n+2):
            # itr(set(), opts, maxLen, ans)
            itr([], opts, maxLen, ans)

        return ans[0]+1

#
# def f(n):
#     if n == 0:
#         return 1
#
#     elif n == 1:
#         return 10
#
#     elif n == 2:
#         return 91
#
#     else:
#         bad = 0
#
#         for i in range(2, n+1):
#             left = n-i
#             bad += max(1, left**9)
#
#         print(bad)
#
#         return 10**n - bad
#
        # return 10**n - sum([9**(x-1) for x in range(2,n+1)])


# f(3)


if __name__ == '__main__':
    s = Solution()

    print(s.countNumbersWithUniqueDigits(0))
    print(s.countNumbersWithUniqueDigits(1))
    print(s.countNumbersWithUniqueDigits(2))
    print(s.countNumbersWithUniqueDigits(3))
    print(s.countNumbersWithUniqueDigits(4))
