
'''
n friends playing a game

Friends a numbered 1 --> n in clockwise order.

Rules of game:
1) Start at first friend
2) count the next k friends including the friend you started at (clockwise)
3) the last friend you counds leaves the circle and looses the game
4) start again but at the friend after the friend that just lost
5) continue until 1 friend is left.

I think we need to model it.

circle = [i for i in range(1, n+1)]
idx = 0

while len(circle) > 2:
    idx = game(idx)

game()


'''

class Solution:
    def findTheWinner(self, n, k):
        circle = [i for i in range(1, n+1)]
        idx = 0

        while len(circle) > 1:
            print(idx)
            idx = (idx+k-1)%len(circle)
            del circle[idx]

        print(circle)

        return circle[0]

s = Solution()

print(s.findTheWinner(5, 2))
print(s.findTheWinner(6, 5))
print(s.findTheWinner(3, 1))
