


class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        maxWater = 2

        while l < r:
            print("l: {} r: {}".format(l, r))


            # calculate area
            if (r-l)*(min(height[l], height[r])) > maxWater:
                maxWater = (r-l)*(min(height[l], height[r]))

            # move goalposts
            if height[l] > height[r]:
                r -= 1

            elif height[r] > height[l]:
                l += 1

            elif height[r] == height[l]:
                if l+1 == r:
                    l += 1
                    continue

                elif l+2 == r:
                    l += 1

                        # elif l+3 == r:
                elif r-l >= 3:
                    if height[l+1] > height[r-1]:
                        l += 1

                    elif height[l+1] < height[r-1]:
                        r -= 1

                    elif height[l+1] == height[r-1]:
                        l += 1

        return maxWater


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
