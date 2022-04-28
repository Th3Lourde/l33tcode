'''
Ok if we don't have negative numbers, we don't need to
worry about anyhting
'''


class Solution:
    def sortedSquares(self, nums):
        if nums[0] >= 0:
            for idx in range(len(nums)):
                nums[idx] *= nums[idx]

            return nums

        elif nums[-1] < 0:
            for idx in range(len(nums)):
                nums[idx] *= nums[idx]

            return nums[::-1]


        else:
            # Find the point where the positive numbers start
            p2 = 0

            while p2 < len(nums) and nums[p2] < 0:
                p2 += 1

            p1 = p2-1

            resp = []

            # p1 represents the smallest positive number
            # p2 represents the largest negative number

            while p1 >= 0 and p2 < len(nums):
                if abs(nums[p1]) < abs(nums[p2]):
                    resp.append(nums[p1]*nums[p1])
                    p1 -= 1

                else:
                    resp.append(nums[p2]*nums[p2])
                    p2 += 1

            while p1 >= 0:
                resp.append(nums[p1]*nums[p1])
                p1 -= 1

            while p2 < len(nums):
                resp.append(nums[p2]*nums[p2])
                p2 += 1

            return resp







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
