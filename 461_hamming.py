'''
Hamming distance is the number
of times the binary representation
of two numbers differ at their
respective indices

not sure how to do that via bit manipulation
'''

class Solution:
    def hammingDistance(self, x, y):
        binX = bin(x)
        binY = bin(y)
        xPtr = len(binX)-1
        yPtr = len(binY)-1

        # print("binX: {}".format(binX))
        # print("binY: {}".format(binY))

        hammingDistance = 0

        while xPtr > 1 or yPtr > 1:
            # print("xPtr: {} | yPtr: {}".format(xPtr, yPtr))
            if xPtr <= 1 or yPtr <= 1:

                if xPtr > 1 and binX[xPtr] == '1':
                    # print("A")
                    hammingDistance += 1

                elif yPtr > 1 and binY[yPtr] == '1':
                    # print("B")
                    hammingDistance += 1

            else:
                if binX[xPtr] != binY[yPtr]:
                    # print("C")
                    hammingDistance += 1

            xPtr -= 1
            yPtr -= 1

        return hammingDistance

print(Solution().hammingDistance(1, 4))
