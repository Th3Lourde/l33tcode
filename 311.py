class Solution:
    def multiply(self, mat1, mat2):
        resp = []

        for r in range(len(mat1)):
            c2 = 0
            row = []

            for _ in range(len(mat1[0])):
                c1 = 0
                r2 = 0
                val = 0
                changedVal = False

                while c1 < len(mat1[0]) and c2 < len(mat2[0]):
                    # print("({},{})*({},{})".format(r,c1,r2,c2))
                    changedVal = True
                    val += mat1[r][c1]*mat2[r2][c2]
                    c1 += 1
                    r2 += 1

                if changedVal:
                    row.append(val)

                c2 += 1

            if len(row) != 0:
                resp.append(row)

        return resp

print(Solution().multiply([[1,-5]], [[12],[-1]]))

print(Solution().multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]]))
