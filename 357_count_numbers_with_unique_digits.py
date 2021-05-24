class Solution:

    def countNumbersWithUniqueDigits_1(self, n):

        if n == 0: return 1
        elif n == 1: return 10

        def itr(terms, in_running, current):
            # Maybe change goal to be == 9
            # if in_running == 0 or 10-current < 1 or current == n:
            if in_running == 0 or current == n:
                return terms+in_running

            else:
                tmp = 0

                for i in range(in_running):
                    tmp += 10-current

                return itr(terms+in_running, tmp, current+1)

        return itr(1, 9, 1)


    def countNumbersWithUniqueDigits_2(self, n):

        ans = [0]

        if n == 0: return 1

        def itr(nums, opts, maxLen, ans):

            if len(nums) == maxLen:

                if nums[0] == 0: return

                if len(nums) == n+1 and nums[0] < 1:
                    # print(nums)
                    ans[0] += 1
                    return

                elif len(nums) == n+1 and nums[0] == 1 and nums[1:] == [0 for i in range(n+1)] :
                    # print(nums)
                    ans[0] += 1
                    return

                elif len(nums) != n+1:
                    # print(nums)
                    ans[0] += 1
                    return

            for i in range(len(opts)):
                if opts[i] not in nums:
                    # nums.add(i)
                    # nums.append(i)
                    itr(nums + [opts[i]], opts[:i]+opts[i+1:], maxLen, ans)
                    # nums.remove(i)
                    # nums.pop()

        opts = [i for i in range(1,10)] + [0]

        for maxLen in range(1, n+2):
            # itr(set(), opts, maxLen, ans)
            itr([], opts, maxLen, ans)

        return ans[0]+1

        # Found the backtracking solution
    def countNumbersWithUniqueDigits_3(self, n):
        if n==0: return 0
        elif n==1: return 1
        elif n==2: return 10

        ans = [1]
        d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

        def itr(k):
            hasDup = False
            for v in d.values():
                if v > 1:
                    hasDup = True

            if hasDup == False:
                ans[0] += 1

            for i in range(0, 10):
                d[i] += 1
                if k-1 >=0:
                    itr(k-1)
                d[i] -= 1

        for i in range(1,10):
            d[i] += 1
            itr(n-1)
            d[i] -= 1

        return ans[0]

        # Math
    def countNumbersWithUniqueDigits(self, n):
        if n == 0: return 0
        if n == 1: return 10
        if n == 2: return 91
        v = 9
        t = 81
        ans = 10+81
        for i in range(3,n+1):
            v -= 1
            t *= v
            ans += t
        return ans

'''
10
9*9
9*9*8
9*9*8*7
....
'''



if __name__ == '__main__':
    s = Solution()

    print(s.countNumbersWithUniqueDigits(0))
    print(s.countNumbersWithUniqueDigits(1))
    print(s.countNumbersWithUniqueDigits(2))
    print(s.countNumbersWithUniqueDigits(3))
    print(s.countNumbersWithUniqueDigits(4))
    print(s.countNumbersWithUniqueDigits(5))
