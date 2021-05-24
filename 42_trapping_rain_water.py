class Solution:
    # 0(n)
    def trap(self, height):
        water = 0
        maxHeight = 0
        tmpW = 0

        for i in range(len(height)):

            if height[i] >= maxHeight:
                maxHeight = height[i]
                water += tmpW
                tmpW = 0
            else:
                tmpW += maxHeight-height[i]


        if tmpW != 0:
            maxHeight = 0
            tmpW = 0

            for i in range(len(height)-1, -1, -1):
                if height[i] > maxHeight:
                    maxHeight = height[i]
                    water += tmpW
                    tmpW = 0
                else:
                    tmpW += maxHeight-height[i]

        return water

s = Solution()

print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))

'''
[0,1,0,2,1,0,1,3,2,1,2,1]
                 ^


water = 4
maxheight = 2
tmpW = 0

What if we go left and then go right?

[5,5,1,7,1,1,5,2,7,6]


'''
