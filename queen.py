

def queensAttacktheKing(queens, king):

    # This will be by row
    board = {}

    # Populate board
    for i in range(len(queens)):
        try:
            board[queens[i][0]].append(queens[i][1])
        except:
            board[queens[i][0]] = queens[i][1]

    # Now that board has been populated:
    k = king

    for i in range(len(queens)):
        q = queens[i]








    if q[0] == k[0]:
        return True
    elif q[1] == k[1]:
        return True

    elif q[0] > k[0] and q[1] > k[1]:
        # Quad 1
        pos = [q[0]-1,q[1]-1]

        while q[0] > k[0] and q[1] > k[1]:
            if pos == k:
                return True
            elif pos != k:
                pos[0] -= 1
                pos[1] -= 1
                # Check that this space isn't occupied



    elif q[0] > k[0] and q[1] < k[1]:
        # Quad 2
        pos = [q[0]-1,q[1]+1]

        while q[0] > k[0] and q[1] < k[1]:
            if pos == k:
                return True
            elif pos != k:
                pos[0] -= 1
                pos[1] += 1
                # Check that this space isn't occupied


    elif q[0] < k[0] and q[1] > k[1]:
        # Quad 3
        pos = [q[0]-1,q[1]-1]

        while q[0] < k[0] and q[1] > k[1]:
            if pos == k:
                return True
            elif pos != k:
                pos[0] -= 1
                pos[1] -= 1
                # Check that this space isn't occupied

    elif q[0] < k[0] and q[1] < k[1]:
        # Quad 4
        # Quad 3
        pos = [q[0]-1,q[1]+1]

        while q[0] < k[0] and q[1] < k[1]:
            if pos == k:
                return True
            elif pos != k:
                pos[0] += 1
                pos[1] += 1
                # Check that this space isn't occupied


    # Have special case for (0,0)
