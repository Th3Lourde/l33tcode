
class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)

        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])

        return cost[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([10,15,20]))
    print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
