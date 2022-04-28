class Solution:
    def checkSubarraySum_1(self, nums, k):
        prev_sums = {0:-1}
        run = 0

        for idx in range(len(nums)):
            run += nums[idx]

            if k != 0:
                run = run % k

            if run in prev_sums:
                if (idx-prev_sums[run]>1):
                    return True
            else:
                prev_sums[run] = idx

        return False

    def checkSubarraySum(self, nums, k):
        d = dict()
        d[0] = -1
        sums = 0

        for i in range(len(nums)):
            sums+=nums[i]
            sums = sums%k

            if(sums in d):
                # if(i-d[sums]>1):
                print("d | {}".format(d))
                print("i | {}".format(i))
                print("d[sums] | {}".format(d[sums]))
                print(i-d[sums])
                if i != 0 and i > d[sums]:
                    print(i-d[sums])
                    return(True)
            else:
                d[sums] = i

        return(False)


print(Solution().checkSubarraySum([1,0], 2))
print(Solution().checkSubarraySum([0], 1))

print(Solution().checkSubarraySum([5,0,0,0], 3))

print(Solution().checkSubarraySum_1([5,0,0,0], 3))

print(Solution().checkSubarraySum([23,2,4,6,6], 7))
print(Solution().checkSubarraySum_1([23,2,4,6,6], 7))

print(Solution().checkSubarraySum([0], 1))
print(Solution().checkSubarraySum([23,2,4,6,7], 6))
print(Solution().checkSubarraySum([23,2,6,4,7], 6))
print(Solution().checkSubarraySum([23,2,6,4,7], 13))
