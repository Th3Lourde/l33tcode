

class Solution:

    def subsets_test(self, nums):
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i] + [n])
        return res




        
    def subsets(self, nums):

        if nums == []:
            return [[]]

        ans = []

        empty = set()

        tmp = [empty]

        for i in range(len(nums)+1):
            if i == 0:
                ans.append([])


            elif i > 0 and i < len(nums):
                ans, tmp = self.generate_subsets_size_i(ans, nums, tmp)

            elif i == len(nums):
                ans.append(nums)

        return ans


    def generate_subsets_size_i(self, ans, n, prev):

        new_prev = []

        for i in range(len(prev)):
            iters = set(n) - prev[i]

            iters = list(iters)

            for j in range(len(iters)):
                term = prev[i]

                if set(list(term)+[iters[j]]) not in new_prev:
                    new_prev.append(set(list(term) + [iters[j]]))
                    ans.append(list(term) + [iters[j]])


        return ans, new_prev

        # for i in range(len(prev)):
        #
        #     # Get rid of all of the elements
        #     # already in the subset
        #     iters = set(n) - set(prev[i])
        #
        #     # print(list(iters))
        #     # print(set(n[0:i+1]))
        #
        #     tmp2 = set(n[0:i])
        #     # iters2 = iters-set(n[0:i])
        #     # print(iters-tmp2)
        #     iters2 = iters-tmp2
        #
        #     iters2 = list(iters2)
        #
        #     # print("tmp: {}".format(prev))
        #     # print("iters: {}".format(iters))
        #     # print("subtracting: {}".format(set(n[0:i+1])))
        #     # print("iters2: {}".format(iters2))
        #     # print("")
        #
        #
        #     for j in range(len(iters2)):
        #         term = prev[i]
        #         # print(term)
        #         new_prev.append(term + [iters2[j]])
        #         ans.append(term + [iters2[j]])
        #     #     print(term + [iters2[j]])
        #
        #
        # return ans, new_prev

if __name__ == '__main__':
    s = Solution()


    # s.generate_subsets_size_n([ set([]),set([1],[2],[3] ]), [1,2,3], [ [1], [2], [3] ] )

    print(s.subsets([3,2,1]))
    # s.subsets([3,2,1])
    # s.subsets([1,2,3] )

    print(s.subsets_test([3,2,1]))
