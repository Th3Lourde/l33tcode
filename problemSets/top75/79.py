class Solution:
    def exist(self, board, word):
        cache = {}
        rows = len(board)
        cols = len(board[0])
        maxIdx = len(word)-1

        def itr(r,c,idx,seen):
            if idx >= maxIdx:
                return True

            # print("{}|{}|{}|{}".format(r,c,idx,seen))
            # print(cache)

            # if (r,c,idx) in cache:
            #     return cache[(r,c,idx)]

            resp = False

            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if word[idx+1] == board[nr][nc] and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        tmp = board[nr][nc]
                        board[nr][nc] = "#"
                        if itr(nr,nc,idx+1,seen):
                            return True
                            resp = True
                            break
                        seen.remove((nr,nc))
                        board[nr][nc] = tmp

            cache[(r,c,idx)] = resp
            return cache[(r,c,idx)]


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and itr(r,c,0,set({(r,c)})):
                    return True

        return False

print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))

'''
["A","B","C","E"]
["S","F","E","S"]
["A","D","E","E"]

"ABCESEEEFS"
  ^


'''
