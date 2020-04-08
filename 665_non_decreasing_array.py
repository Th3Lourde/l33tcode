

class Solution:
    def checkPossibility(self, nums):
        canSwap = True
        z = 0

        if len(nums) == 1:
            return True

        while z <= len(nums)-1:

            if z == 0 and nums[z] > nums[z+1]:
                nums[z] = nums[z+1]-1
                canSwap = False

            elif z > 0 and z <= len(nums)-2 and nums[z] > nums[z+1]:

                if z+1 == len(nums)-1 and canSwap:
                    return True

                elif canSwap and nums[z-1] <= nums[z+1]:
                    nums[z] = nums[z-1]
                    canSwap = False

                elif canSwap and z <= len(nums)-3:
                    if nums[z] > nums[z+2]:
                        return False

                    canSwap = False

                else:
                    return False

            z += 1

        return True

if __name__ == '__main__':
    s = Solution()

    testCases = [
        [[], True],
        [[1], True],
        [[4,2,3], True],
        [[4,2,1], False],
        [[1,2,4,5,3], True],
        [[2,3,3,2,4], True],
        [[2,3,3,2,1], False],
        [[2,3,1,5,4], False],
        [[1,2,3,4,5,3,4,5], False],
        [[1,2,3,4,5,4,4,5,6], True],
        [[1,2,3,4,5,4,4,5,1], False],
    ]

    z = 0
    passed = True

    for tc in testCases:
        resp = s.checkPossibility(tc[0])

        if resp != tc[1]:
            passed = False
            print("[failed test case {}] wanted {} got {}".format(z, tc[1], resp))
            break

        z += 1

    if passed:
        print("[passed all testcases :)]")
