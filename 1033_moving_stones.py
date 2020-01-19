


class Solution:
    def numMovesStones(self, a, b, c):
        # 1 Sort the stones least to greatest
        tmp = [a,b,c]

        for j in range(2):
            for i in range(len(tmp)-1):
                if tmp[i] > tmp[i+1]:
                    tmpII = tmp[i+1]
                    tmp[i+1] = tmp[i]
                    tmp[i] = tmpII

        # Ok, now that the stones are sorted,
        # we can continue

        # 2) Figure out what stone is the one
        # we will be 'moving'
        # print(tmp)

        if (tmp[1]-tmp[0] == 1) and (tmp[2]-tmp[1] == 1):
            return [0,0]


        if (tmp[1]-tmp[0]) >= (tmp[2]-tmp[1]):
            # Will be moving tmp[0]
            # 1) Get dist of second endpoint

            if tmp[2]-tmp[1] > 2:
                # This should not happen
                return [2, tmp[2]-tmp[1]-1 + tmp[1]-tmp[0]-1]

            elif tmp[2]-tmp[1] == 2:
                # min = 1
                # max = tmp[1]-tmp[0] + 1
                return [1, tmp[1]-tmp[0]+1-1]

            elif tmp[2]-tmp[1] == 1:
                return [1, tmp[1]-tmp[0]-1]



        elif (tmp[1]-tmp[0]) < (tmp[2]-tmp[1]):
            # Will be moving tmp[2]
            if tmp[1]-tmp[0] > 2:
                return [2, tmp[1]-tmp[0]-1 + tmp[2]-tmp[1]-1]

            elif tmp[1]-tmp[0] == 2:
                return [1, tmp[2]-tmp[1]+1-1]

            elif tmp[1]-tmp[0] == 1:
                return [1, tmp[2]-tmp[1]-1]












if __name__ == '__main__':
    s = Solution()

    a = 7
    b = 4
    c = 1


    print(s.numMovesStones(a,b,c))
