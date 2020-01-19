

class Solution:

    def sortColors(self, nums):
        counts = [0,0,0]

        for i in range(nums):
            if nums[i] == 0:
                counts[0] += 1
            elif nums[i] == 1:
                counts[1] += 1
            elif nums[i] == 2:
                counts[2] += 1

        z = 0

        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[z] = i
                z += 1

        print(nums)


if __name__ == '__main__':
    s = Solution()

    in = [2,0,2,1,1,0]

    s.sortColors(in)
