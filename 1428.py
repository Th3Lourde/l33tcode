class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        rows, cols = binaryMatrix.dimensions()
        resp = float('inf')

        # print("dims of matrix: {},{}".format(rows,cols))
        # print("{}".format(binaryMatrix.get(rows,cols)))

        def binarySearch(row):
            l = 0
            r = cols-1

            while l < r:
                m = (l+r)//2

                if binaryMatrix.get(row, m) < 1:
                    l = m+1
                else:
                    r = m

            return l

        for r in range(rows):
            tCol = binarySearch(r)

            # print("tCol of row {} is {}".format(r, tCol))

            resp = min(resp, binarySearch(r))

        if resp == float('inf'):
            return -1

        return resp
