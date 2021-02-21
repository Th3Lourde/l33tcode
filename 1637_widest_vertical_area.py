[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

'''
Yea this is totally a shit problem.
Just calculate the greatest horizontal
distance between two adjacent points.

'''

class Solution:
    def maxWidthOfVerticalArea(self, points):
        d = {}

        for point in points:
            if point[0] not in d:
                d[point[0]] = True

        keys = list(d.keys())

        keys.sort(reverse=True)

        ans = 0 

        for i in range(len(keys)-1):
            diff = keys[i] - keys[i+1]
            if diff > ans:
                ans = diff

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
    print(s.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
