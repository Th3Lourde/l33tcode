import math

class Solution:
    def sumSubarrayMins(self, A):
        ans = 0

        for i in range(len(A)):
            for j in range(i,len(A)):
                term = A[i:j+1]

                tmp = min(term)
                ans += tmp

        return ans


        # return 10**(int(math.log(ans, 10))) + ans%10


if __name__ == '__main__':
    # Return power of ten + what is left

    s = Solution()

    # print(s.sumSubarrayMins([3,1,2,4]))
    print(s.sumSubarrayMins([85]))
