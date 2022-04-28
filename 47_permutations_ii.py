class Solution:
    def permuteUnique(self, nums):
        setOfTuples = set()

        def generatePermutations(perm, opts):
            if len(opts) == 0:
                setOfTuples.add(tuple(perm))
                return

            for idx in range(len(opts)):
                generatePermutations(perm+[opts[idx]], opts[:idx]+opts[idx+1:])

        generatePermutations([], nums)

        ans = []

        for t in setOfTuples:
            ans.append(list(t))

        return ans

print(Solution().permuteUnique([1,1,2]))
print(Solution().permuteUnique([1,2,3]))
