'''
Ok so basic reading comprehension.
Read the algo that we will be implementing.

Given two arr[int].

From left to right: targ[index[i]] = nums[i]

This will be way easier if we know the length
of the list.

One clarifying question that I would have is if:
len(nums) == len(targArray).

This doesn't need to be true, however I am wondering
if it is.

This is true. Also it looks like insert has an interesting
meaning within this context.

Let's say that we have: [a,b,c,d,e,f,g]

If we insert(x) at index i, we get:

[0:i] + [x] + [i:]

It is also given to us that the insertion operations will
be valid. I don't really know what this means. One assumption
would be that this guarantees a certain max value of index[i]
∋ index[i] <= len(targArray).

I don't know if this is true.

Let's test it and see what happens.

Ok so the condition is that index[i] should be ≤ i.

So my assumption is correct. We could just use
.insert(), however let's actually code this thing.

So we start with []

ans = []

for i in range(len(nums)):
    idx = index[i]

        # If we are inserting at the end
    if idx == len(ans):
        ans.append(nums[id])

    else:
        ans = ans[:idx] + [nums[id]] + ans[idx:]

return ans

Ok so I have passed all test cases.








'''

class Solution:
    def createTargetArray(self, nums, index):
        ans = []

        for i in range(len(nums)):
            idx = index[i]

                # If we are inserting at the end
            if idx == len(ans):
                ans.append(nums[i])

            else:
                ans = ans[:idx] + [nums[i]] + ans[idx:]

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))

    print(s.createTargetArray([1,2,3,4,0], [0,1,2,3,0]))

    print(s.createTargetArray([1], [0]))
