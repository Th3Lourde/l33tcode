class Solution:
    def permuteUnique(self, nums):
        permutations = set()

        def itr(perm, opts):
            if len(opts) == 0:
                permutations.add(tuple(perm))

            for idx, opt in enumerate(opts):
                itr(perm+[opt], opts[:idx]+opts[idx+1:])

        itr([], nums)

        ans = []

        for perm in permutations:
            ans.append(list(perm))

        return ans

print(Solution().permuteUnique([1,1,2]))
print(Solution().permuteUnique([1,2,3]))
