
class Solution:

    # However this is not the case :)
    def maxProduct(self, nums) -> int:
        if len(nums) < 1:
            return "Error, array not large enough"

        ans = nums[0]

        for i in range(len(nums)):
            tmp = nums[i]
            if tmp > ans:
                ans = tmp

            for j in range(i+1, len(nums)):
                if nums[j] != 1:
                    tmp *= nums[j]
                    if tmp > ans:
                        ans = tmp

                if nums[j] == 0:
                    break

        return ans

    def maxProduct3(self, nums) -> int:
        if len(nums) < 1:
            return "Error, array not large enough"

        r = nums[0]
        imax = r
        imin = r

        for i in range(1, len(nums)):
            if nums[i] < 0:
                # True if both imax and
                # imin are positive
                # Also True if one if imin
                # is neg and imax is pos
                tmp = imax
                imax = imin
                imin = imax

            imax = max(nums[i], imax*nums[i])
            imin = max(nums[i], imin*nums[i])

            r = max(r, imax)

        return r



    # Uses prefix product and suffix product
    # Very smart solution, I understand it
    # wonder if there's a way to do it that
    # doesn't rely on prior knowledge of prefix
    # suffix products
    def maxProduct2(self, A):
        B = A[::-1]

        # print("{}\n".format(A))
        # print("A: {}".format(A))
        # print("B: {}".format(B))


        for i in range(1, len(A)):
            # print(A[i])
            A[i] *= A[i - 1] or 1
            # print(A)
            B[i] *= B[i - 1] or 1

        # print(A)
        # print(B)


        return max(A + B)


    def maxProduct1(self, nums) -> int:
        # Assuming that subarray must have len() == 2
        if len(nums) < 2:
            return "Error, input not big enough"

        ans = nums[0] * nums[1]

        for i in range(1, len(nums)-1):
            if (nums[i]*nums[i+1]) > ans:
                ans = nums[i]*nums[i+1]
        return ans


if __name__ == '__main__':
    a = [-1,-4,0,9,8]

    s = Solution()
    # r = s.maxProduct(a)
    r = s.maxProduct3(a)
    print(r)
    # r = s.maxProduct2(a)
    # print(r)
