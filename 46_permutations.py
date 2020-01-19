import math

class Solution:

    def permute_1(self, nums):
        ans = []
        def iter(a, l, r):
            # print("a: {} l: {} r:{}".format(a,l,r))
            if l == r:
                # print(a)
                tmp = a.copy()
                ans.append(tmp)

                if len(ans) == math.factorial(len(nums)):
                    return ans

            else:
                for i in range(l, r+1):
                    a[l], a[i] = a[i], a[l]
                    r = iter(a, l+1, r)
                    a[l], a[i] = a[i], a[l]

            return r

        ans = iter(nums, 0, len(nums)-1)
        return ans

    def permute(self, nums):

        def permutate(perm, options):
            if options == []:
                ans.append(perm.copy())

            elif options != []:
                for j in range(len(options)):
                    perm.append(options[j])
                    tmp = options[j]
                    del options[j]

                    permutate(perm, options)

                    options.insert(j, tmp)
                    del perm[-1]

        ans = []

        permutate([], nums)

        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
