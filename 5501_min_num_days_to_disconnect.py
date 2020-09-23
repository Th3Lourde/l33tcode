'''
Another kind of DP problem? Backtracking?

For each zero, find the min days it would take
to create an island.

backtracking algo for changing the zero.

Pick a direction, disconnect it if 1,

opts: where we have gone so far, set of positions
to avoid direct backtracking, or looping through already
seen locations once again.



(loc:[int, int], seen )

opts = [(-1,0), (1,0), (0,-1), (0,1)]

for opt in opt:

[row, col]

'''

def itr(loc, seen):
    opts = [(-1,0), (1,0), (0,-1), (0,1)]

    for opt in opts:
        if 0 <= loc[0]+opt[0] <= len(grid) and 0 <= loc[1]+opt[1] <= len(grid[0]) and (loc[0]+opt[0], loc[1]+opt[1]) not in seen:
            # if within x-bounds, y-bounds and have not been seen before
            switch = grid[loc[0]][loc[1]] == 1
            grid[loc[0]+opt[0]][loc[1]+opt[1]] = 0
            # check if island? Call from zero that we started at?
            # call function to keep going
            if switch:
                grid[loc[0]+opt[0]][loc[1]+opt[1]] = 0

            ...
