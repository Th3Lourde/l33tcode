class Solution:
    def maxArea(self, height):
        maxHeight = float('-inf')
        l = 0
        r = len(height)-1

        while l < r:
            maxHeight = max(maxHeight, min(height[l], height[r]) * (r-l))

            if height[l] < height[r]:
                # Move l right until at a bigger value
                tmp = height[l]
                l += 1

                while l < r and tmp >= height[l]:
                    l += 1

            else:
                # Move r left until at a bigger value
                tmp = height[r]
                r -= 1

                while l < r and tmp >= height[r]:
                    r -= 1

        return maxHeight

'''
[1,8,6,2,5,4,8,3,7]
 l
                 r

7
'''

print(Solution().maxArea([1,1]))
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
