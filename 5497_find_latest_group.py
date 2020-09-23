'''
Given a list of zeros.

As we loop through arr,
arr[i] represents the zero that
we are going to be setting to one.

We want to return the latest step,
where there exists an adjacent grouping
of ones of size m.

use sliding window in order to check
for ones.


Don't start until we have done a certain
number of steps.

Then use a sliding window in order to check.

Is there any better way to check for combos?

Umm, I don't think so.

We'll find out :)

'''

class Solution:
    def findLatestStep(self, arr, m):
        binNum = [0 for i in range(len(arr))]
        comp = [1 for i in range(m)]
        ans = -1

        for i in range(len(arr)):

            binNum[arr[i]-1] = 1

            # Check list for combos.

            for j in range(len(binNum)-m+1):
                subSet = binNum[j*m:j*m + m+1]


                if subSet == comp:
                    # We have found a potential
                    # candidate, look right,
                    # look left
                    LHS = True

                    if j > 0 and binNum[j*m-1] == 1:
                        LHS = False

                    RHS = True

                    if j*m+m < len(binNum)-1 and binNum[j*m + m+1] == 1:
                        RHS = False

                    if LHS and RHS:
                        ans = i+1
                        print("{} | [{},{}] | j: {} True".format(binNum, j*m, j*m+m, j))

                    else:
                        print("{} | [{},{}] | j: {} False".format(binNum, j*m, j*m+m, j))

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.findLatestStep([3,5,1,2,4], 1))

    print(s.findLatestStep([3,1,5,4,2], 2))

    print(s.findLatestStep([2,1], 2))
#     [1,2]
# 1

    print(s.findLatestStep([1,2], 1))
