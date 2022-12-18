class Solution:
    def minStickers(self, stickers, target):
        m = len(stickers)
        mp = [[0]*26 for y in range(m)]
        n = len(mp)
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1

        dp = {}
        dp[""] = 0

        def helper(dp, mp, target):
            if target in dp:
                return dp[target]

            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1

            ans = float('inf')

            for i in range(n):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue

                newTarget = ''

                for j in range(26):
                    if tar[j] > mp[i][j]:
                        newTarget += chr(ord('a')+j)*(tar[j]-mp[i][j])

                # now that we have our new target, make a recursive
                # call to see if this works
                tmp = helper(dp, mp, newTarget)
                if tmp != -1:
                    # b/c it's the amount of stickers needed to
                    # create the new target string, plus the sticker that
                    # we used to get to the new target string

                    ans = min(ans, tmp+1)

            dp[target] = -1 if ans == float('inf') else ans
            return dp[target]

        return helper(dp, mp, target)





print(Solution().minStickers( ["multiply","swim","love","father","shape","rich","new","fill","history"], "operateform" ))
print(Solution().minStickers(["bring","plane","should","against","chick"], "greatscore"))
print(Solution().minStickers(["with","example","science"], "thehat"))
