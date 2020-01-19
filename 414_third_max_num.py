


class Solution:
    def thirdMax(self, nums):
        terms = 0
        maxes = [None, None, None]

        for i in range(len(nums)):
            if terms == 0:
                maxes[0] = nums[i]
                terms += 1
                # print(maxes)

            elif terms == 1:
                if maxes[0] > nums[i]:
                    maxes[1] = nums[i]
                    terms += 1
                    # print(maxes)

                elif maxes[0] < nums[i]:
                    maxes[1] = maxes[0]
                    maxes[0] = nums[i]
                    terms += 1
                    # print(maxes)


            elif terms == 2:
                if maxes[0] < nums[i]:
                    maxes[2] = maxes[1]
                    maxes[1] = maxes[0]
                    maxes[0] = nums[i]
                    terms += 1

                elif maxes[1] < nums[i] and nums[i] != maxes[0]:
                    maxes[2] = maxes[1]
                    maxes[1] = nums[i]
                    terms += 1

                elif maxes[1] > nums[i] and nums[i] != maxes[0]:
                    maxes[2] = nums[i]
                    terms += 1

            elif terms == 3:

                if (maxes[0] < nums[i] and maxes[1] < nums[i]) and (maxes[2] < nums[i]):
                # if maxes[2] < nums[i]:
                    maxes[2] = maxes[1]
                    maxes[1] = maxes[0]
                    maxes[0] = nums[i]

                elif (maxes[0] > nums[i] and maxes[1] < nums[i]) and (maxes[2] < nums[i]):
                    maxes[2] = maxes[1]
                    maxes[1] = nums[i]

                elif (maxes[0] > nums[i] and maxes[1] > nums[i]) and (maxes[2] < nums[i]):
                    maxes[2] = nums[i]

        print(maxes)


        if terms < 3:
            return maxes[0]

        elif terms == 3:
            return maxes[2]
        # return True


if __name__ == '__main__':
    s = Solution()

    # nums = [2,2,3,1]

    # nums = [1,2,2]

    nums = [1,2,2,5,3,5]

    print(s.thirdMax(nums))
