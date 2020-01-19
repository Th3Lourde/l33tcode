


class Solution:


    def isBoomerang(self, points):
        A, B, C = points
        AB = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(0.5)
        BC = ((B[0] - C[0])**2 + (B[1] - C[1])**2)**(0.5)
        AC = ((A[0] - C[0])**2 + (A[1] - C[1])**2)**(0.5)
        
        return not(AB == BC + AC or BC == AB + AC or AC == AB + BC)

    def isBoomerang_1(self, points):

        # 1) Make sure that the points are distinct

        if (points[0] == points[1]) or (points[0] == points[2]) or (points[1] == points[2]):
            return False


        try:
            s1 = abs(points[0][1]-points[1][1])/abs(points[0][0]-points[1][0])
            s1 *= 100

        except:
            s1 = -123


        try:
            s2 = abs(points[0][1]-points[2][1])/abs(points[0][0]-points[2][0])
            s2 *= 100

        except:
            s2 = -123


        try:
            s3 = abs(points[1][1]-points[2][1])/abs(points[1][0]-points[2][0])
            s3 *= 100

        except:
            s3 = -123


        # s3 = abs(points[1][1]-points[2][1])/abs(points[1][0]-points[2][0])

        # 2) Make sure that the points are not in a line

        if (s1 == s2) and (s1 == s3):

            return False

        print("s1: {} s2: {} s3: {}".format(s1, s2, s3))


        return True


if __name__ == '__main__':
    s = Solution()

    # inp = [[1,1],[2,3],[3,2]]
    # print(s.isBoomerang(inp))
    #
    #
    # inp = [[1,1],[2,2],[3,3]]
    # print(s.isBoomerang(inp))

    # inp = [[0,0],[0,2],[2,1]]

    inp = [[52,86],[12,65],[24,71]]


    print(s.isBoomerang(inp))
