

class Solution:

    # smart-solution
    def threeSum(self, nums):
        ans = []
        history = {}

        if len(nums) < 3:
            return []

        nums.sort()

        if nums[0] > 0:
            return []

        elif nums[-1] < 0:
            return []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                return ans

            elif nums[i] <= 0:
                for j in range(i+1, len(nums)-1):

                    for z in range(j+1, len(nums)):
                        if (nums[i] == 0 and nums[j] != 0):
                            # [0, >0, >0]
                            # can't equal zero
                            return ans

                        elif nums[i]+nums[j]+nums[z] == 0:

                            triple = [nums[i],nums[j],nums[z]]
                            triple.sort()

                            try:
                                history[str(triple)]
                            except:
                                history[str(triple)] = 1
                                ans.append([ nums[i], nums[j], nums[z] ])

                            # We found our triple, time to iterate
                            # on i or j, after this we are still
                            # looking for the same z-value, which
                            # doesn't actually help b/c we don't
                            # care about repeats
                            break

        return ans

    # brute-force
    def threeSum_1(self, nums):
        ans = []
        history = {}

        if len(nums) < 3:
            print("nums not big enough")
            return []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for z in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[z] == 0:

                        triple = [nums[i],nums[j],nums[z]]
                        triple.sort()

                        try:
                            history[str(triple)]
                        except:
                            history[str(triple)] = 1
                            ans.append([ nums[i], nums[j], nums[z] ])

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
