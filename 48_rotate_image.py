


class Solution:
    # God-Tier Solution
    # This dude just swapped the diags
    # I swapped every item one time more than needed
    # Kinda confused how this works. Come back later
    def rotate(self, matrix):
        for i in range (len(matrix)):
            for j in range (i, len(matrix)):
                # print("swap({},{})".format(matrix[i][j], matrix[j][i]))
                a= matrix[i][j]
                b= matrix[j][i]
                matrix[i][j] = b
                matrix[j][i] = a




    # Looks like a mess,
    # gets really good results in l33tcode
    #
    def rotate_1(self, matrix):

        for i in range(len(matrix)//2):
            start = matrix[i][i:len(matrix)-i]

            tmp = []
            z = 0
            for j in range(i, len(matrix)-i):
                tmp.append(matrix[j][(-1)*i-1])
                matrix[j][(-1)*i-1] = start[z]
                z += 1

            tmp2 = matrix[(-1)*i-1][i:len(matrix)-i]

            tmp2[-1] = tmp[-1]

            matrix[(-1)*i-1][i:len(matrix)-i] = tmp[::-1]

            tmp = tmp2

            tmp2 = [0]*(len(matrix)-2*i)
            z = 0
            tmp2[-1] = tmp[0]

            for j in range(i, len(matrix)-i):
                if j+1 < len(matrix)-i:
                    tmp2[z] = matrix[j][i]
                matrix[j][i] = tmp[z]
                z += 1

            matrix[i][i:len(matrix)-i] = tmp2[::-1]

def printM(m):
    for i in range(len(m)):
        print(m[i])
    print("")


if __name__ == '__main__':
    s = Solution()
    m  = [
            ["a","b","c","d","e","f"],
            ["g","h","i","j","k","l"],
            ["m","n","o","p","q","r"],
            ["s","t","u","v","w","x"],
            ["y","z","1","2","3","4"],
            ["5","6","7","8","9","0"],
        ]

    printM(m)

    print("")

    s.rotate(m)

    printM(m)
