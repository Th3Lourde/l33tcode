
class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1

        numbers_sum = numbers[l]+numbers[r]

        while numbers_sum != target:
            numbers_sum = numbers[l]+numbers[r]

            if numbers_sum > target:
                r -= 1

            elif numbers_sum < target:
                l += 1

        return [l+1, r+1]

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,3,4], 6))
print(Solution().twoSum([-1,0], -1))
