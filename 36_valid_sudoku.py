



class Solution:
    def isValidSudoku(self, board):
        def inValid(subset):
            # print("subset: {}".format(subset))
            d = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}

            for element in subset:
                if element != ".":
                    if d[element] < 1:
                        d[element] += 1
                    else:
                        return True

            return False

        # Check rows
        for i in range(len(board)):
            if inValid(board[i]):
                return False

        # Check columns
        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])

            if inValid(col):
                return False


        # Check squares
        for i in range(3):
            for j in range(3):
                start = [3*i, 3*j]
                sqr = []
                for z in range(3):
                    sqr += board[start[0]+z][start[1]:start[1]+3]

                # print("sqr: {}".format(sqr))

                if inValid(sqr):
                    return False

        return True




'''
[
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]
]


[
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

'''
