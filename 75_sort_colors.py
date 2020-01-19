
class Solution:

    def sortColors(self, nums):
        i1 = 0
        i2 = 1
        i3 = len(nums)-1

        while i2 < i3:
            t1 = nums[i1]
            t2 = nums[i2]
            t3 = nums[i3]

            while t1 == 0:
                i1 += 1
                i2 += 1
                t1 = nums[i1]
                t2 = nums[i2]

            while t3 == 2:
                i3 -= 1
                t3 = nums[i3]

            if t1 == 2 and t3 == 0:
                nums[i1] = 0
                nums[i3] = 2
                i1 += 1
                i2 += 1
                i3 -= 1

            elif t1 == 1 and t3 == 0:
                nums[i1] = 0
                nums[i3] = 1
                i1 += 1
                i2 += 1

            elif t1 == 2 and t3 == 1:
                nums[i1] = 1
                nums[i3] = 2
                i3 -= 1

            elif t1 == 1 and t3 == 1:

                '''
                t2 == 0
                t2 == 1
                t2 == 2
                '''

                if t2 == 0:
                    nums[i1] = 0
                    nums[i2] = 1
                    i1 += 1
                    i2 += 1

                elif t2 == 2:
                    nums[i3] = 2
                    nums[i2] = 1
                    i3 -= 1

                elif t2 == 1:
                    while t2 < t3 and t2 == 1:
                        i2 += 1
                        t2 = nums[i2]

        print(nums)




    def sortColors_1(self, nums):
        counts = [0,0,0]

        for i in range(len(nums)):
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

    inp = [2,0,2,1,1,0]

    s.sortColors(inp)
