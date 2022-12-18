class Solution:
    def permute(self, nums):
        permutations = set()

        def itr(subset, opts):
            if len(opts) == 0:
                permutations.add(tuple(subset))
                return

            for idx, opt in enumerate(opts):
                itr(subset+[opt], opts[:idx]+opts[idx+1:])

        itr([], nums)

        resp = []

        for permutation in permutations:
            resp.append(list(permutation))

        return resp

print(Solution().permute([1]))
print(Solution().permute([0,1]))
print(Solution().permute([1,2,3]))
