


class Solution:

    def numIslands(self, grid):
        ans = 0
        visited = set()

        def isLand(coord):
            if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]) and grid[coord[0]][coord[1]] == "1" and (coord[0], coord[1]) not in visited:
                return True

            else:
                return False

        def traverse(coord):
            stack = [coord]

            while stack:
                coord = stack.pop()
                visited.add(coord)

                if isLand((coord[0]-1, coord[1])):
                    stack.append((coord[0]-1, coord[1]))

                if isLand((coord[0]+1, coord[1])):
                    stack.append((coord[0]+1, coord[1]))

                if isLand((coord[0], coord[1]-1)):
                    stack.append((coord[0], coord[1]-1))

                if isLand((coord[0], coord[1]+1)):
                    stack.append((coord[0], coord[1]+1))

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                coord = grid[row][column]

                if coord == "1" and (row, column) not in visited:
                    ans += 1
                    traverse((row, column))

        return ans


        # This solution works
    def numIslands_2(self, grid):
        ans = 0
        map = {}

        for r in range(len(grid)):
            # print(grid[r])
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    isIsland = True
                    connected = False

                    if c > 0:
                        try:
                            if map[str([r,c-1])]:
                                connected = map[str([r,c-1])]
                                isIsland = False
                                map[str([r,c])] = connected

                        except:
                            pass

                    if r > 0:
                        try:
                            if map[str([r-1,c])]:
                                isIsland = False
                                if connected != map[str([r-1,c])]:
                                    if connected:
                                        # The one we replace is dependent upon which one is smaller

                                        if map[str([r,c-1])] > map[str([r-1,c])]:
                                            map[str([r,c-1])][0] =  map[str([r-1,c])][0]
                                            map[str([r,c])] = map[str([r-1,c])]

                                        elif map[str([r,c-1])] < map[str([r-1,c])]:
                                             map[str([r-1,c])][0] = map[str([r,c-1])][0]
                                             map[str([r,c])] = map[str([r,c-1])]

                                        ans -= 1

                                    elif not connected:
                                        map[str([r,c])] = map[str([r-1,c])]

                                elif connected == map[str([r-1,c])]:
                                    map[str([r,c])] = connected

                        except:
                            pass

                    if isIsland:
                        ans += 1
                        map[str([r,c])] = [ans]

        # print("")
        #
        #
        # print(list(map.values()))

        return ans

    def numIslands_1(self, grid):

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    isIsland = True

                    if c > 0:
                        if grid[r][c-1] == 1:
                            isIsland = False

                    if isIsland and r > 0:
                        if grid[r-1][c] == 1:
                            isIsland = False

                    if isIsland:
                        ans += 1


        return ans




if __name__ == '__main__':
    s = Solution()

    testCases = [
        [[], 0],
        [[[]], 0],
        [[["1"]], 1],
        [[["1","0","0"],["1","0","0"],["1","0","1"]], 2],
        [[["1","0","0"],["1","0","1"],["1","0","1"]], 2],
        [[["1","0","1"],["1","0","1"],["1","0","1"]], 2],
        [[["1","0","1"],["1","1","1"],["1","0","1"]], 1],
        [[["1","0","0","0","1"],["1","0","1","0","1"],["1","0","0","0","1"],["1","0","1","0","1"],["1","0","0","0","1"]], 4],
        [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],1],
        [[["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]],3],
        [[["1","1","1","1","1","1","1","1","1"],["1","0","0","0","0","0","0","0","1"],["1","0","1","0","1","0","1","0","1"],["1","0","1","1","1","1","1","0","1"],["1","0","1","0","1","0","1","0","1"],["1","0","0","0","0","0","0","0","1"],["1","1","1","1","1","1","1","1","1"]],2]
    ]

    passed = True
    z = 1

    for testCase in testCases:
        resp = s.numIslands(testCase[0])

        if resp != testCase[1]:
            passed = False
            print("[failed test case {}] wanted {} got {}".format(z, testCase[1], resp))
            break

        z += 1

    if passed:
        print("[passed all test cases] :)")
