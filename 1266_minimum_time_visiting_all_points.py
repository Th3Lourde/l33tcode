
class Solution:
    def minTimeToVisitAllPoints(self, points):
        time = 0
        current = points[0]

        for i in range(1, len(points)):
            x_dist = abs(points[i][0] - current[0])
            y_dist = abs(points[i][1] - current[1])

            time += max(x_dist, y_dist)

            current = points[i]

        return time


if __name__ == '__main__':
    s = Solution()

    # points = [[1,1],[3,4],[-1,0]]

    points = [[3,2],[-2,2]]

    print(s.minTimeToVisitAllPoints(points))
