

class Solution:
    def combinationSum(self, candidates, target):
        minE = min(candidates)
        ans = []

        if minE > target:
            return ans

        elif minE == target:
            return [[minE]]

        elif minE < target:
            end = target//minE + 1
            end *= minE


        for i in range(1, end+1): # Could optimize end
            size = i # looking for sum of elements of size i

            if size == 1:
                if target in candidates:
                    ans.append([target])

            elif size == 2:
                elems = list(candidates)
                elems.sorted()

                while elems[-1] >= target: # Find all elements > target, remove them
                    del elems[-1]

                for z in range(len(elems)):
                    if target-elems[z] in candidates:
                        ans.append([elems[z], target-elems[z]])

            elif size > 2:
                ...
