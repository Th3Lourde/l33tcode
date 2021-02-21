'''
Given an integer nums sorted in an increasing order:
return an array of the squares of each number sorted in increasing order

[-4,-1,0,3,10]

So what we want to do is sort by abs value instead of by value.

If there are positive numbers, we want to sort by mag.
If there are not positive numbers, just flip the order and square
everything.

If the first term is >= 0, then case two

Case 0:
First term is positive, just square everything, return

Case 1:
First term is neg, nothing is >= 0, flip list, square, return

Case 2:
We have a mix of positive and negative values
1) Find the first val >= 0
2) Then use a two pointer approach to sort by abs(x)
3) Then square everything and return

'''

class Solution:
    def sortedSquares(self, nums):
        # First figure out what case we have
        if nums[0] >= 0:
            # square everything and return
            for i in range(len(nums)):
                nums[i] = nums[i]**2
            return nums

        elif nums[-1] < 0:
            # reverse list, square everything, return
            nums = nums[::-1]
            for i in range(len(nums)):
                nums[i] = nums[i]**2
            return nums
        else:
            # We have a neg and a pos
            # sort by abs(x)

            p1 = 0
            p2 = len(nums)-1

            i = 0
            while nums[i] < 0:
                i += 1

            while p1 <= i:
                if nums[p2-1] <= abs(nums[p1]) <= nums[p2]:
                    nums.insert(p2, abs(nums[p1]))
                    p1 += 1
                    # p2 -= 1

                elif abs(nums[p1]) > nums[p2]:
                    nums.insert(p2+1, abs(nums[p1]))
                    p1 += 1
                    # p2 -= 1

                else:
                    p2 -= 1

            nums = nums[p1:]

            for i in range(len(nums)):
                nums[i] = nums[i]**2
            return nums

if __name__ == '__main__':
    s = Solution()

    s.sortedSquares([-4,-1,0,3,10])
    s.sortedSquares([-7,-3,2,3,11])
    s.sortedSquares([-7,-3,-2])
    s.sortedSquares([2,3,11])


    s.sortedSquares([-2,-1,3])
    s.sortedSquares([-2,-1,1])
    s.sortedSquares([-1,1])
    s.sortedSquares([-1,0])
    s.sortedSquares([-2,-1,0])
    s.sortedSquares([-3,-2,-1,0])
    s.sortedSquares([-3,-2,-1,1])
    s.sortedSquares([-3,-2,-1,0,1,4])
    s.sortedSquares([-3,-2,-1,0,1,4,9])
    s.sortedSquares([-5,-3,-2,-1,0,1,4,9])
    s.sortedSquares([-6,-5,-3,-2,-1,0,1,4,9])
