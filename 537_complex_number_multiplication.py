'''
Given two strings that represent complex numbers,
Return the string that represents their multiplication.

so:
a + bi
c + di

a*c + (ad + cb)i

Depending on what the values
are for d,b, either adding to right
term or subtracting from left term.

Part one: get the number of terms,
split over addition for both.

The first thing that I should probably
do is get two lists with integers in both
of them. Then construct my answer based upon
that.

For ℜ.
if - == [0], do -1*int([1:])
else, do int([:])

For 𝑖.
if - == [0], do -1*int([1:-1]) ← last term is 'i'
elif - != [0], do int([:-1])

Let's get that squared away and then come back

Ok so that works. Now what?

1) Get the first term squared away.

Ok so I just 'grokked' it. Didn't do
any test cases. Got it right.
'''



class Solution:
    def complexNumberMultiply(self, a, b):
        nums = []

        for s in [a,b]:

            A = s.split("+")

            # print(A)

            tmp = []

            if A[0][0] == "-":
                tmp.append(-1*int(A[0][1:]))

            elif A[0][0] != "-":
                tmp.append(int(A[0]))


            if A[1][0] == "-":
                tmp.append(-1*int(A[1][1:-1]))

            elif A[1][0] != "-":
                tmp.append(int(A[1][:-1]))

            # print(tmp)

            nums.append(tmp)

        # print(nums)
        middle = -1*nums[0][1]*nums[1][1]

        ans = []
        ans.append(nums[0][0]*nums[1][0] + middle)
        ans.append(nums[0][0]*nums[1][1] + nums[0][1]*nums[1][0])

        return "{}+{}i".format(ans[0], ans[1])


if __name__ == '__main__':
    s = Solution()
    s.complexNumberMultiply("1+1i", "1+1i")
    s.complexNumberMultiply("1+-1i", "1+-1i")
    s.complexNumberMultiply("100+-10i", "10+104i")
