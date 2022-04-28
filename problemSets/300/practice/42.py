'''
[0,1,0,2,1,0,1,3,2,1,2,1]
                 ^

So two passes

have a bound var

|       | |
|   |   ||| |
|_|_||_|||||||
         ^

ans = 7
bound = 3
tmpW = 0

If we hit a val with a greater, adjust bound and add tmpW to ans
'''

class Solution:
    def trap(self, height):
        bound = 0
        ans = 0
        tmpW = 0

        for idx in range(len(height)):
            if height[idx] >= bound:
                ans += tmpW
                bound = height[idx]
                tmpW = 0
            else:
                tmpW += bound-height[idx]

        bound = 0
        tmpW = 0

        for idx in range(len(height)-1, -1, -1):
            if height[idx] > bound:
                ans += tmpW
                bound = height[idx]
                tmpW = 0
            else:
                tmpW += bound-height[idx]

        return ans

print(Solution().trap([0,1,0,2,1,0,1,3,2,3,1,2,1]))
