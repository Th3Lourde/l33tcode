import math


class Solution:
    def smallestDivisor(self, nums, threshold):
        '''
        List integers called nums
        integer threshold

        For some reason, this doesn't decrease the run-time
        enough. I wonder if there's some number theory thing
        that I don't understand well enough

        Haven't tried this code yet, maybe the check with if
        element < threshold b4 entering for-loop will help?
        seems like a very slight improvement in run-time
        '''

        divisor = 0
        sum = threshold+1

        while sum > threshold:
            divisor += 1
            sum = 0

            if math.ceil(nums[i]/divisor) < threshold:
                for i in range(len(nums)):
                    sum += math.ceil(nums[i]/divisor)

                    if sum > threshold:
                        # If the sum is already bigger than threshold
                        # go to next divisor
                        print('hi')
                        break

        return divisor



if __name__ == '__main__':
    s = Solution()
    # print(s.smallestDivisor([1,2,5,9], 6))
    print(s.smallestDivisor([70,3,5,7,11], 11))
