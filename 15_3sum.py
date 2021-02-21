

class Solution:

    '''
    Ok so we are using the goalpost approach
    first term can't be a repeat
    second term can't be a repeat
    if first, second can't be a repeat, then neither can third :)
    '''

    def threeSum_3(self, nums):
        ans = []
        nums.sort()

        for i in range(len(nums)):

            # Also navigate to avoid duplicates

            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = nums[i]*(-1)

            s,e = i+1, len(nums)-1

            while s < e:

                if nums[s]+nums[e] == target:
                    ans.append([nums[i], nums[s], nums[e]])

                    '''
                    [1,1,1,1,2,2,2,3]
                    '''

                    while nums[s] == nums[s+1] and s<e:
                        s += 1

                    s += 1


                elif nums[s]+nums[e] > target:
                    e -= 1

                elif nums[s]+nums[e] < target:
                    s += 1

        return ans

    # smart-solution
    def threeSum_2(self, nums):
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


        # 1.10.21
    def threeSum(self, arr):
        ans = []
        arr.sort()
        n = len(arr)

        for i in range(n-1):
            if arr[i] == arr[i+1]:
                continue

            targ = (-1)*arr[i]
            l, r = i+1, n-1

            while l < r:
                if arr[l]+arr[r] == targ:
                    ans.append([arr[l], arr[r], arr[i]])
                    l += 1
                    # Do something with l
                    while l < r and arr[l] == arr[l-1]: l += 1

                if arr[l]+arr[r] < targ:
                    l += 1
                else:
                    r -= 1
        return ans




if __name__ == '__main__':
    s = Solution()

    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([]))
    print(s.threeSum([0]))
