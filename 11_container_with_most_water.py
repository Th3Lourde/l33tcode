
'''
You are given an array (height) that contains integers
Select two integers (i1, i2) from the array such that

abs(i1-i2)*min(height[i1], height[i2])

is maximized

Method 1: brute force:
find all possible solutions, return the best one
Time complexity: O(n^2)
Space complexity: O(c)
'''



class Solution:

    # Brute-Force
    # Time complexity: O(n^2)
    # Space complexity: O(c)
    # Given that n is at least two,
    # which means that len(height) >= 2
    # got TLE, so this is the right solution,
    # just isn't fast enough
    def maxArea_TLE(self, height):
        if len(height) < 2:
            print("Houston, we have a problem")

        ans = None

        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                tmp =  abs(i-j)*min(height[i],height[j])

                if ans == None:
                    ans = tmp
                elif tmp > ans:
                    ans = tmp


        print("ans: {}".format(ans))

    '''
    have ans = height[0], height[-1]
    have ml for max left (initialized at 0)
    have mr for max right (initialized at leng(height)-1)
    move left bound up by one, check area, if area greater, update answer, update ml
    move right bound up by one, check area, if area greater, update answer, update mr
    stop when tmpl == tmpr
    tmpl = iterator that starts on left
    tmpr = iterator that starts on right
    '''

    def maxArea(self, h):
        def calcArea(i,j,h1,h2):
            return abs(i-j)*min(h1,h2)

        l = 0
        mL = 0
        r = len(h)-1
        mR = len(h)-1
        ans = calcArea(l,r,h[l],h[r])

        while l < r:
            l += 1
            tmp = calcArea(l,mR,h[l],h[mR])
            if tmp > ans:
                ans = tmp
                mL = l

            r -= 1
            tmp = calcArea(mL,r,h[mL],h[r])
            if tmp > ans:
                ans = tmp
                mR = r

        return ans


        # modern, correct
    def maxArea(self, h):
        ans = float('-inf')
        l, r = 0, len(h)-1

        while l < r:
            water = (r-l)*min(h[l], h[r])
            if water > ans:
                ans = water

            # Update Goal Posts
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    # [2,3,4,5,18,17,6]
