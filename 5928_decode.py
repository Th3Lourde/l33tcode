'''
ch   ie   pr|rows=3
   ^

c h _ _





---------------
c h
  i e
    p r

so len(str)/rows = number of columns
'''

class Solution:
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText

        cols = int(len(encodedText)/rows)

        idx = 0
        matrix = []

        for r in range(rows):
            col = []
            for c in range(cols):
                col.append(encodedText[idx])
                idx += 1
            matrix.append(col)

        # for row in matrix:
        #     print(row)

        col = 0
        ans = ""

        while col < len(matrix[0]) :
            # if matrix[0][col] == "":
            #     return ans

            ans += matrix[0][col]

            tmpCol = col + 1
            row = 1

            while row < len(matrix) and tmpCol < len(matrix[0]):
                 # if matrix[row][tmpCol] == "":
                 #     return ans

                ans += matrix[row][tmpCol]
                tmpCol += 1
                row += 1

            col += 1

        return ans.rstrip()





Solution().decodeCiphertext("ch   ie   pr", 3)
Solution().decodeCiphertext("iveo    eed   l te   olc", 4)
