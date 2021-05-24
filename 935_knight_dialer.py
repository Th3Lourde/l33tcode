'''
1 2 3
4 5 6
7 8 9
* 0 #

d = {
    0: 4,6
    1: 6,8
    2: 7,9
    3: 4,8
    4: 0,3,9
    5:
    6: 0,1,7
    7: 2,6
    8: 1,3
    9: 2,4
}

i = 0

for k in d[i]:
    d[n][i] += d[n-1][k]

0
dp[4]+dp[6] | 1+1 | 2


         0 1 2 3 4 5 6 7 8 9
dp  = [1,1,1,1,1,1,1,1,1,1,1]
dpT = [0,2,2,2,2,3,0,3,2,2,2]




'''
class Solution:
    def knightDialer(self, n):
        d = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4],
        }

        dp = [1 for _ in range(11)]
        dp[5] = 0

        for _ in range(n-1):
            dpT = [0 for _ in range(11)]

            for k in range(10):
                for z in d[k]:
                    dpT[k] += dp[z]

            dp = dpT

        return sum(dp) % (10**9 + 7)



s = Solution()

print(s.knightDialer(1)) # 10
print(s.knightDialer(2)) # 20
print(s.knightDialer(3)) # 46
print(s.knightDialer(4)) # 104
print(s.knightDialer(3131)) # 136006598
