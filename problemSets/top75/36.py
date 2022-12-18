class Solution:
    def isValidSudoku(self, board):
        rows = len(board)
        cols = len(board[0])

        # 1) Check all rows
        for r in range(rows):
            rowSet = set()

            for c in range(cols):
                if board[r][c] in rowSet and board[r][c] != ".":
                    # print("A")
                    return False

                rowSet.add(board[r][c])

        # 2) Check all cols
        for c in range(cols):
            colSet = set()

            for r in range(rows):
                if board[r][c] in colSet and board[r][c] != ".":
                    # print("B")
                    return False

                colSet.add(board[r][c])

        # 3) Check all boxes
        boxes = [
        (0,0), (0,3), (0,6),
        (3,0), (3,3), (3,6),
        (6,0), (6,3), (6,6)
        ]

        for sR, sC in boxes:
            boxSet = set()

            for r in range(sR, sR+3):
                for c in range(sC, sC+3):
                    if board[r][c] in boxSet and board[r][c] != ".":
                        # print("C")
                        return False

                    boxSet.add(board[r][c])

        return True

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
