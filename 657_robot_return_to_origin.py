'''
Robot starts at position (0,0).
Given a sequence of its moves, judge
whether or not the robot ends up at (0,0)

Have a position list that gets updated
as we move through the string.

return pos == [0,0]

pos = [0,0]

if "U":
    pos[1] += 1

elif "D":
    pos[1] -= 1

elif "L":
    pos[0] -= 1

elif "R":
    pos[0] += 1


'''

class Solution:
    def judgeCircle(self, moves):
        pos = [0, 0]

        for m in moves:
            if m == "U":
                pos[1] += 1

            elif m == "D":
                pos[1] -= 1

            elif m == "L":
                pos[0] -= 1

            elif m == "R":
                pos[0] += 1

        return pos == [0, 0]


if __name__ == '__main__':
    s = Solution()

    print(s.judgeCircle("UD"))
    print(s.judgeCircle("LL"))
    print(s.judgeCircle(""))
    print(s.judgeCircle("ULRDU"))
    print(s.judgeCircle("ULRD"))
    
