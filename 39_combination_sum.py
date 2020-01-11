
'''
So this works, however it exceeds the time limit.
Counts as a victory in my book, time to make it
more efficient
'''

class Solution:

    def combinationSum_2(self, candidates, target):
        import copy

        def recursive(options, target, run):
            if target == 0:
                run.sort()
                if (run not in ans):
                    ans.append(run)

            elif target > 0:
                for i in range(len(options)):
                    if target-options[i] >= 0:
                        newRun = copy.deepcopy(run)
                        newRun.append(options[i])
                        recursive(options, target, newRun)


        ans = []
        tmp = list(candidates)
        run = []

        recursive(tmp, target, run)

        return ans

    # This works, is slow
    def combinationSum_2(self, candidates, target):
        import copy

        def recursive(options, target, run):
            if (sum(run) == target):
                run.sort()
                if (run not in ans):
                    ans.append(run)

            elif sum(run) < target:
                for i in range(len(options)):
                    newRun = copy.deepcopy(run)
                    newRun.append(options[i])

                    if sum(newRun) <= target:
                        recursive(options, target, newRun)

        ans = []
        tmp = list(candidates)
        run = []

        recursive(tmp, target, run)

        return ans
    #
    # def combinationSum_1(self, candidates, target):
    #     minE = min(candidates)
    #     ans = []
    #
    #     if minE > target:
    #         return ans
    #
    #     elif minE == target:
    #         return [[minE]]
    #
    #     elif minE < target:
    #         end = target//minE + 1
    #         end *= minE
    #
    #
    #     for i in range(1, end+1): # Could optimize end
    #         size = i # looking for sum of elements of size i
    #
    #         if size == 1:
    #             if target in candidates:
    #                 ans.append([target])
    #
    #         elif size == 2:
    #             elems = list(candidates)
    #             elems.sorted()
    #
    #             while elems[-1] >= target: # Find all elements > target, remove them
    #                 del elems[-1]
    #
    #             for z in range(len(elems)):
    #                 if target-elems[z] in candidates:
    #                     ans.append([elems[z], target-elems[z]])
    #
    #         elif size > 2:
    #             ...
    #

if __name__ == '__main__':
    s = Solution()

    # print(s.combinationSum([2,3,6,7], 7))

    print(s.combinationSum([2,3,5], 8))
