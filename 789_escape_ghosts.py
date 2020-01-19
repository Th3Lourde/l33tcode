import math


class Solution:
    # def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    def escapeGhosts1(self, ghosts, target) -> bool:
        my_dist = math.sqrt( (target[0])**2 + (target[1])**2 )

        for i in range(len(ghosts)):
            tmp = math.sqrt( (target[0]-ghosts[i][0])**2 + (target[1]-ghosts[i][1])**2 )

            if my_dist >= tmp:
                return False

        return True

    def escapeGhosts(self, ghosts, target) -> bool:
        my_dist = self.dist([0,0], target)

        for i in range(len(ghosts)):
            tmp = self.dist(ghosts[i], target)

            if my_dist >= tmp:
                return False

        return True


    def dist(self, pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1] )


    def dist1(self, pos, goal):

        if pos == [0,0]:
            ans = abs(goal[0]) + abs(goal[1])
            return ans

        if goal == [0,0]:
            ans = abs(pos[0]) + abs(pos[1])
            return ans


        if goal[0] == 0:
            x = abs(pos[0])

        elif goal[0] < 0:

            if pos[0] == 0:
                x = abs(goal[0])

            elif pos[0] < 0:
                x = abs(goal[0] - pos[0])

            elif pos[0] > 0:
                x = goal[0]*(-1) + pos[0]

        elif goal[0] > 0:
            if pos[0] == 0:
                x = goal[0]

            elif pos[0] < 0:
                x = goal[0] + abs(pos[0])

            elif pos[0] > 0:
                x = abs(goal[0] - pos[0])


        if goal[1] == 0:
            y = abs(pos[1])

        elif goal[1] < 0:

            if pos[1] == 0:
                y = abs(goal[1])

            elif pos[1] < 0:
                y = abs(goal[1] - pos[1])

            elif pos[1] > 0:
                y = goal[1]*(-1) + pos[1]

        elif goal[1] > 0:

            if pos[1] == 0:
                y = goal[1]

            elif pos[1] < 0:
                y = goal[1] + abs(pos[1])

            elif pos[1] > 0:
                y = abs(goal[1] - pos[1])

        return x+y













if __name__ == '__main__':
    s = Solution()

    # ghosts = [[1,0], [0,3]]
    #
    # target = [0,1]
    #
    # print(s.escapeGhosts(ghosts, target))
    #
    #
    #
    #
    # ghosts = [[1,0]]
    #
    # target = [2,0]
    #
    # print(s.escapeGhosts(ghosts, target))
    #
    # ghosts = [[2, 0]]
    # target = [1, 0]
    # print(s.escapeGhosts(ghosts, target))

    pos = [2,-2]
    goal = [-6,9]

    print(s.dist(pos, goal))

    pos = [-2,2]
    goal = [6,-9]
    print(s.dist(pos, goal))
