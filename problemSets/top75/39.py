class Solution:
    def combinationSum(self, candidates, target):
        solves = set()
        n = len(candidates)
        candidates.sort()

        def itr(idx, picks, s):
            if s == target:
                solves.add(tuple(picks))
                return

            for i in range(idx, n):
                if s+candidates[i] <= target:
                    itr(i, picks+[candidates[i]], s+candidates[i])

        itr(0, [], 0)

        resp = []

        for solve in solves:
            resp.append(list(solve))

        return resp

print(Solution().combinationSum([2], 1))
print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))
