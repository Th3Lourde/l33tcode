class Solution:
    # top-down, correct, slow
    def findLongestChain_1(self, pairs):
        dp = {}
        pairs.sort()
        # print(pairs)

        def itr(dp, idx, maxE):
            if idx >= len(pairs):
                return 0

            if maxE in dp:
                return dp[maxE]

            max_chain = 0
            for i in range(idx, len(pairs)):
                if maxE < pairs[i][0]:
                    max_chain = max(max_chain, itr(dp, i+1, pairs[i][1])+1)

            dp[maxE] = max_chain

            return max_chain


        ans = itr(dp, 0, float('-inf'))
        # print(dp)
        return ans

    def findLongestChain(self, pairs):
        chain = 0
        pairs.sort(key = lambda x: x[1])

        lim = float('-inf')

        for l, r in pairs:
            if lim < l:
                lim = r
                chain += 1
                
        return chain

s = Solution()


print(s.findLongestChain([[9,10],[9,10],[4,5],[-9,-3],[-9,1],[0,3],[6,10],[-5,-4],[-7,-6]]))
print(s.findLongestChain([[1,2], [2,3], [3,4]]))
print(s.findLongestChain([[1,2], [3,5], [3,4], [5,6], [6,7], [7,8]]))
