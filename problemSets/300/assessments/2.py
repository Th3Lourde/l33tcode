'''
Write a function that returns the min time
in seconds to go from point a to point b.

Compute how much time it takes to get from point
a to point b, for all points, in order

return answer

Given a, given b

(ax, ay), (bx, by)

while ax < bx and


(3,3) --> (3,4)

time = 2

1 < 3 and 1 < 4:
    (1,1) += (1,1)
    time += sqrt(2)

while 3 == 3 and 3 != 4:
    3 += 1
    time += 1



'''



class Solution:
    def minTimeToVisitAllPoints(self, points):
        total_time = 0

        def time_between_points(x1,y1,x2,y2):
            x_dist = abs(x1-x2)
            y_dist = abs(y1-y2)
            diags = min(x_dist, y_dist)
            singles = max(x_dist, y_dist) - min(x_dist, y_dist)

            return diags + singles

        for idx in range(len(points)-1):
            x1,y1 = points[idx]
            x2,y2 = points[idx+1]

            total_time += time_between_points(x1,y1,x2,y2)

        return total_time
