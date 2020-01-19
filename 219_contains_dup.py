class Solution:

    def containsNearbyDuplicate(self, nums, k) -> bool:

        if nums == []:
            return False

        d = {nums[0]:[0]}

        for i in range(1,len(nums)):
            try:
                d[nums[i]].append(i)
                vals = d[nums[i]]

                for j in range(len(vals)-1):
                    if (vals[j] != i) and (abs(i-vals[j]) <= k):
                        return True
            except:
                d[nums[i]] = [i]

        return False


    def containsNearbyDuplicate1(self, nums, k) -> bool:
        # Check to see if there exists i,j s.t. nums[i] == nums[j]
        # Also |j-k| <= k

        # i equals all but the last nums[i] in list
        for i in range(0, len(nums)-1):
            # Get the number of nums[i]s that
            # we can check
            n = len(nums)-1-i

            if n > k:
                n = i + k
            elif n <= k:
                n = i + n

            for j in range(i+1, n+1):
                if nums[i] == nums[j]:
                    return True

        return False


if __name__ == '__main__':
    s = Solution()

    # nums = [1,2,3,1]
    # k = 3
    # r = s.containsNearbyDuplicate(nums,k)
    # print(r)

    # nums = [1,0,1,1]
    # k = 1
    # r = s.containsNearbyDuplicate(nums,k)
    # print(r)


    # nums = [1,2,3,1,2,3]
    # k = 2
    r = s.containsNearbyDuplicate(nums,k)
    print(r)
