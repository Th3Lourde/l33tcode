
class Solution():
    def queensAttacktheKing(self, queens, king):
        board = {}

        # 1) Put all of the queens into a
        # dictonary
        for i in range(len(queens)):
            try:
                board[queens[i][0]].append(queens[i][1])
            except:
                board[queens[i][0]] = [queens[i][1]]

        # 2) Figure out which queens will hit
        dirs = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,1], [-1,-1], [1,-1]]
        ans = []
        i = 1

        while len(dirs) != 0:
            remove = []

            for j in range(len(dirs)):
                n_p = [king[0] + i*dirs[j][0], king[1]+ i*dirs[j][1]]

                try:
                    board[n_p[0]]

                    if n_p[1] in board[n_p[0]]: # Found match, save (x,y), remove direction
                        ans.append(n_p)
                        remove.append(dirs[j])
                    elif n_p[0] > 7 or n_p[0] < 0 or n_p[1] > 7 or n_p[1] < 0: # If pos is off board, remove
                        remove.append(dirs[j])

                except:

                    if n_p[0] > 7 or n_p[0] < 0 or n_p[1] > 7 or n_p[1] < 0: # If pos is off board, remove
                        remove.append(dirs[j])


            for k in range(len(remove)):
                dirs.remove(remove[k])

            i += 1


        return ans



if __name__ == '__main__':
    s = Solution()
    # queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
    # king = [3,3]

    queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
    king = [3,4]



    r = s.queensAttacktheKing(queens,king)
    print(r)
