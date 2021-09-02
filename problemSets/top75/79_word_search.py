'''
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
'''


class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def backtrack(i,j,idx,seen):
            if idx >= len(word):
                return True

            for r,c in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
                if 0 <= r < rows and 0 <= c < cols and (r,c) not in seen:
                    if board[r][c] == word[idx]:
                        seen.add((r,c))

                        if backtrack(r,c,idx+1,seen):
                            return True

                        seen.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r,c,1,set({(r,c)})):
                    return True

        return False
