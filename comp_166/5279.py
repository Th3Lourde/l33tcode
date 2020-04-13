


class Solution:
    def subtractProductAndSum(self, n):
        '''
        Goal here is: given integer n, return diff between product of digits and sum of digits
        '''

        n = list(str(n))

        prod = 1
        sum_1 = 0


        for i in range(len(n)):
            prod *= int(n[i])
            sum_1 += int(n[i])

        return prod-sum_1


if __name__ == '__main__':
    s = Solution()

    print(s.subtractProductAndSum(234))
