
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

    def maxArea(self, height):

        def getArea(i, j, n1, n2):
            return abs(i-j)*min(n1,n2)

        ml = tmpl = 0
        mr = tmpr = len(height)-1
        ans = getArea(ml, mr, height[ml], height[mr])
        print("Current ans: {}".format(ans))

        while tmpl < tmpr:
            tmpl += 1
            tmp = getArea(tmpl, mr, height[tmpl], height[mr])

            if tmp > ans:
                ml = tmpl
                ans = tmp
                print("updated ans: {}".format(ans))

            tmpr -= 1
            tmp = getArea(ml, tmpr, height[ml], height[tmpr])

            if tmp > ans:
                mr = tmpr
                ans = tmp
                print("updated ans: {}".format(ans))

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    # [2,3,4,5,18,17,6]
