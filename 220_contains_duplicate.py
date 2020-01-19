


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if t < 0:
            return False

        # elif t == 0:
        #     for i in range(len(nums)):
        #         if abs(nums[i]-nums[i]) <= k:
        #             return True

        elif t > 0:
            for i in range(len(nums)-1):

                for j in range(i+1, len(nums)):

                    if (abs(nums[i]-nums[j]) <= t) and (abs(i-j) <= k):
                        return True

                    elif not(abs(i-j) <= k):
                        break

        return False




if __name__ == '__main__':
    s = Solution()

    # nums = [1,2,3,1]
    # k = 3
    # t = 0

    # nums = [1,0,1,1]
    # k = 1
    # t = 2

    # nums = [1,5,9,1,5,9]
    # k = 2
    # t = 3

    print(s.containsNearbyAlmostDuplicate(nums,k,t))
