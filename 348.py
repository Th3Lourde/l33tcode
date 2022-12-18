class TicTacToe:

    def __init__(self, n):
        self.n = n
        self.won = False
        m = [[0]*n for _ in range(n)]
        self.m = m


    def move(self, row, col, player):
        if self.won:
            return 1

        self.m[row][col] = player

        # Check columns
        colRun = True
        for r in range(self.n):
            if self.m[r][col] != player:
                colRun = False

        # Check rows
        rowRun = True
        for c in range(self.n):
            if self.m[row][c] != player:
                rowRun = False

        # Check diags
        diag1Run = True
        for i in range(self.n):
            if self.m[i][i] != player:
                diag1Run = False

        r, c = self.n-1, 0
        diag2Run = True
        while r >= 0 and c < self.n:
            if self.m[r][c] != player:
                diag2Run = False

            r -= 1
            c += 1

        self.won = colRun or rowRun or diag1Run or diag2Run

        if self.won:
            return player

        return 0
