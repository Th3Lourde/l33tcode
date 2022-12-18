class Solution:
    def subsets(self, nums):
        sets = set({})

        def itr(elements, opts):
            sets.add(tuple(elements))

            for idx, opt in enumerate(opts):
                itr(elements+[opt], opts[idx+1:])

        itr([], nums)

        resp = []

        for e in sets:
            resp.append(list(e))

        return resp

print(Solution().subsets([1,2,3]))
