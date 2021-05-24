'''
[1,8,6,2,5,4,8,3,7]
   l             r
'''

class Solution:
    def maxArea(self, h):
        area = min(h[0],h[1])

        l = 0
        r = len(h)-1

        while l < r:
            # area = max(area, (min(h[l], h[r])*r-l))
            water = min(h[l], h[r])*(r-l)

            if water > area:
                area = water

            if h[l] <  h[r]:
                l += 1

            else:
                r -= 1

        return area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
