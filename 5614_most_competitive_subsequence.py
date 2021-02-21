'''
Given []int, most mostCompetitive subsequence is
a sublist of nums.

So we calculate a score, score is ∀ x ∈ nums, score +=  x_n - x_n-1

You can remove as many elements are you need to.

What is the mostCompetitive subsequence that you can come up with?

[1,3,5]
[1,3,4] ← More competitive

[1,2,5] ← More competitive
[1,3,4]

This is true b/c we evaluate on the first point where the two differ.

1) We care about creating lists that contain as small of numbers as
possible. The numbers don't need to be in order, they just need to be
small.

We care about all numbers, s.t. we can create a subsequence of k or more
behind them.

Get all possible sub-sequences, with length k or more. If more than k,
iterate through how we can remove the largest elements.

We should also keep track of the smallest number that corresponds to a valid
sequence?

I'm leaning towards a brute force method.

1) Find all sequences of length k. Store the most competitive.


So we should write a function that compares two sequences to see which is more
competitive.

Do one run, with subsequence == k.
Then try to beat that run.

Keep track of what the 'winning' subsequence is, and
iterate through possible values.

So two iterations.

[2,4,3,3,5,4,9,6] | k = 4
        (       )

ans = 2,4,3,3



[2,4,3,3,5,4,9,6] | k = 4
(       )

2,4,3,3
  ^

idx = 0

Once we have 'beaten' it, out of the remaining
elements, remove the max element until length of
sublist is workable.


[2, 3, 3, ]

1) Write isMoreCompetitive
2) First pass → get most competitive with sliding window len = k
3) Second + pass. If we make a change/'win', re-run again. If re-run and
    no change, we are done.

'''

'''
To Review:

def mostCompetitive(self, nums, k):
    to_remove = len(nums) - k
    stack = []

    for x in nums:
        while stack and x < stack[-1] and to_remove:
            to_remove -= 1
            stack.pop()
        stack.append(x)

    for _ in range(to_remove):
        stack.pop()

    return stack
'''



class Solution:

    # is a more competitive than b?
    def isMoreCompetitive(self, a, b):
        if len(a) != len(b):
            print("Error, len()'s do not match'")
            return "Error"

        for i in range(len(a)):
            if a[i] == b[i]:
                continue
            elif a[i] < b[i]:
                return True
            else:
                return False

        return False

    def refined(self, nums, i, a, ans):
        if i >= len(nums):
            if len(a) == len(ans) and self.isMoreCompetitive(a, ans) == False:
                return False, None

            elif len(a) != len(ans):
                return False, None

            else:
                return True, a

        elif i < len(nums) and len(ans)-len(a) <= len(nums)-i :
            boolA, respA = self.refined(nums, i+1, a+[nums[i]], ans)
            boolB, respB = self.refined(nums, i+1, a, ans)

            if boolA == True and boolB == True:
                if self.isMoreCompetitive(respA, respB):
                    return True, respA
                else:
                    return True, respB

            elif boolA == True:
                return boolA, respA

            elif boolB == True:
                return True, respB

            else:
                return False, None

        else:
            return False, None



    def mostCompetitive(self, nums, k):

        if len(nums) < k :
            print("length mismatch @ init")
            return False

        ans = list(nums[0:k])
        tmp = list(nums[0:k])
        i = k

        # Initial pass
        while i < len(nums):
            # print(tmp)
            del tmp[0]
            # print(tmp)
            tmp.append(nums[i])
            # print(tmp)
            if self.isMoreCompetitive(tmp, ans):
                ans = list(tmp)
            i += 1
            # print("ans: {}, tmp:{}".format(ans, tmp))
            # print("")

        # Pass 2
        shouldContinue = True
        idx = 0

        foundAnswer, updateAns = self.refined(nums, 0, [], ans)

        if foundAnswer == True:
            return updateAns

        return ans




if __name__ == '__main__':
    s = Solution()

    print(s.mostCompetitive([3,5,2,6], 2))
    print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))
    print(s.mostCompetitive([84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71], 24))
    print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))


    [11,52,57,91,47,95,86,46,87,47,70,56,54,61,89,44,3,73,1,7,87,48,17,25,49,54,6,72,97,62,16,11,47,34,68,58,14,36,46,65,2,15]
18
