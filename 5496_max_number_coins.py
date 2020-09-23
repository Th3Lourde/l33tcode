

class Solution:
    def maxCoins(self, piles):

        ans = 0

        l = 0
        r = len(piles)-2

        piles.sort()

        while l < r:
            ans += piles[r]
            l += 1
            r -= 2

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.maxCoins([2,4,1,2,7,8]))
    print(s.maxCoins([2,4,5]))
    print(s.maxCoins([9,8,7,6,5,1,2,3,4]))
