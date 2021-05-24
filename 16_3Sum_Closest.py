class Solution:
    # Can do better than 0(n² log(n))
    def threeSumClosest_1(self, nums, target):
        def binSearch(data, val):
            # print("data: {} | target: {}".format(data, val))
            lo, hi = 0, len(data) - 1
            best_ind = lo
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if data[mid] < val:
                    lo = mid + 1
                elif data[mid] > val:
                    hi = mid - 1
                else:
                    best_ind = mid
                    break
                # check if data[mid] is closer to val than data[best_ind]
                if abs(data[mid] - val) < abs(data[best_ind] - val):
                    best_ind = mid
            return data[best_ind]

        nums.sort()
        # print(nums)

        closestSum = float('inf')

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                # print("i:{}|j:{}".format(i,j))
                bestCombo = binSearch(nums[:i]+nums[i+1:j]+nums[j+1:], target-nums[i]-nums[j])

                if abs(target-(nums[i]+nums[j]+bestCombo)) < abs(target-closestSum):
                    closestSum = nums[i]+nums[j]+bestCombo

        return closestSum

    def threeSumClosest(self, nums, target):
        nums.sort()

        closest = float('inf')

        for i in range(len(nums)-2):
            # print(i)

            j = i+1
            z = len(nums)-1

            while j < z:
                threeSum = nums[i]+nums[j]+nums[z]
                # print(threeSum)

                if abs(target-threeSum) < abs(target-closest):
                    closest = threeSum

                if threeSum > target:
                    z -= 1

                elif threeSum < target:
                    j += 1

                else:
                    break

        return closest


s = Solution()

print(s.threeSumClosest([-1,2,1,-4], 1))


    # [-1,2,1,-4]
'''
[-1,2,1,-4]

target: 1

-4-1+2 = -1, too small l += 1

[-4,-1,1,2]
  ^    l  r
'''
