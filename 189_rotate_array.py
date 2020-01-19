



class Solution:
    def rotate(self, nums, k):
        to_move = []

        for i in range(len(nums)):
            to_move.append(i)

        # to_move now contains all of
        # the indices that we need to
        # adjust


        # If the nums[i]s will end up
        # where they started from
        if k % len(nums) == 0:
            return nums

        # Adjust k s.t. it is within bounds
        if k >= len(nums):
            k = k - len(nums)


        while len(to_move) != 0:
            item = to_move[0]
            val = nums[item]

            while True:

                # z represents the
                # target index, the
                # index of the nums[i]
                # that we are going to
                # swap/replace

                z =  item + k

                if z >= len(nums):
                    z = z - len(nums)


                tmp = nums[z]

                nums[z] = val

                to_move.remove(item)

                if z not in to_move:
                    break

                elif z in to_move:
                    item = z
                    val = tmp

        return nums


if __name__ == '__main__':
    s = Solution()

    nums = [1,2,3,4,5,6,7]
    k = 3

    print(s.rotate(nums,k))

    nums = [-1,-100,3,99]
    k = 2
    print(s.rotate(nums,k))
