
class Solution:
    def exist(self, board, word):

        if len(word) == 0:
            return True

        def findHits(board, start, char, pathE):
            ans = []

            # Look left:
            if start[1] > 0:
                if board[start[0]][start[1]-1] == char:

                    try:
                        pathE[str([start[0], start[1]-1])]

                    except:
                        ans.append([start[0], start[1]-1])

            # Look right:
            if start[1] < len(board[0])-1:
                if board[start[0]][start[1]+1] == char:

                    try:
                        pathE[str([start[0], start[1]+1])]

                    except:
                        ans.append([start[0], start[1]+1])

            # Look up:
            if start[0] < len(board)-1:
                if board[start[0]+1][start[1]] == char:

                    try:
                        pathE[str([start[0]+1, start[1]])]

                    except:
                        ans.append([start[0]+1, start[1]])

            # Look down:
            if start[0] > 0:
                if board[start[0]-1][start[1]] == char:

                    try:
                        pathE[str([start[0]-1, start[1]])]

                    except:
                        ans.append([start[0]-1, start[1]])

            return ans


        def convert(pathZ):
            keys = list(pathZ.keys())

            resp = {}

            for key in keys:
                resp[str(pathZ[key])] = True

            return resp


        # 1) Find all elements on the board that match the first character in word
        start = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    start.append([i,j])


        # 2) Use backtracking to find an appropriate path
        if len(start) == 0:
            return False

        if len(word) == 1:
            return True

        z = 1
        current = start.pop()
        history = []
        pathE = {str(current): True}
        pathZ = {0: current}

        # history = [[] for char in range(len(word))] Check to see if this works later :)

        for char in range(len(word)):
            history.append([])

        history[0] = start

        # z is always positioned over the character that we would like to find.

        while z <= len(word)-1:
            hits = findHits(board, current, word[z], pathE)

            if hits == []:
                # backtrack

                if z-1 >= 0:
                    del pathZ[z-1]

                z -= 1


                while len(history[z]) == 0:

                    if z >= 0:
                        if z-1 >= 0:
                            del pathZ[z-1]

                        z -= 1

                    elif z < 0:
                        return False


                current = history[z].pop()
                pathZ[z] = current

                pathE = convert(pathZ)

                z += 1

            elif hits != []:
                current = hits[0]

                pathE[str(current)] = True
                pathZ[z] = current

                history[z] = hits[1:]
                z += 1

        if z >= len(word)-1:
            return True

        else:
            print("[flag]")
            return False

if __name__ == '__main__':
    s = Solution()

    testCases = [
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCCED", True, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "SEE", True, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCB", False, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "AF", False, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCB", False, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ZBCB", False, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCESEEDAS", True, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCESEEDASA", False, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCESEEDASFC", True, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCESEEDASFCS", False, ],
        [ [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "Z", False, ],
    ]

    board = testCases[0][0]

    print("board:")

    for row in range(len(board)):
        print("   {}".format(board[row]))

    print("")

    passed = True
    z = 1

    for testCase in testCases:
        resp = s.exist(testCase[0], testCase[1])

        if resp != testCase[2]:
            passed = False
            print("[failed test case {}] wanted {} got {}".format(z, testCase[2], resp))
            break

        z += 1

    if passed:
        print("[passed all test cases] :)")


'''
Notes: Ok so the correct solution for this must be a dynamic programming problem. I think this
    because backtracking has pretty much always been the niave solution, so it would make sense
    if there is a better solution out there (to-do tomorrow :D)

    I got this right on my first attempt so I am pretty happy with that. What I am doing "differently"
    is I am, once my code has been written, stepping through my code and trying to figure out where it
    might be broken. This is good practice for having better code quality. In order to decrease the amount
    of work that is done via this method is to write better code initially. This means more writing by hand.
    More thinking and less coding. This should be worth the work. I am looking forward to the day where I
    understand my language well enough to implement something of this complexity correctly the first time.
    Good new is: this is my second time implementing a backtracing solution, and the idea of backtracing,
    as well as the implementation, is something that I organically came up with. Go me.
    L,E.
'''
